import psycopg2
import psycopg2.extras
import os
import logging
from dotenv import load_dotenv

load_dotenv()
logger = logging.getLogger(__name__)


def get_connection() -> psycopg2.extensions.connection:
    """
    Creates and returns a new PostgreSQL database connection.
    Reads the DATABASE_URL from the .env file.
    Returns: psycopg2 connection object
    """
    return psycopg2.connect(os.getenv("DATABASE_URL"))


def fetch_latest_jobs(limit: int = 5) -> list[dict]:
    """
    Fetches the most recently scraped jobs from the database.

    Parameters:
        limit (int): How many jobs to return. Defaults to 5.

    Returns:
        list[dict]: Each dict has keys — title, company, location, salary, job_url
    """
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
    
    try:
        cursor.execute("""
            SELECT title, company, location, salary, job_url
            FROM jobs
            ORDER BY scraped_at DESC
            LIMIT %s
        """, (limit,))
        rows = cursor.fetchall()
        logger.info(f"Fetched {len(rows)} latest jobs from database")
        
        return [dict(row) for row in rows]
    
    except Exception as e:
        logger.error(f"Error fetching latest jobs: {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def search_jobs_by_location(location: str, limit: int = 10) -> list[dict]:
    """
    Searches for jobs where the location field contains the given search term.
    Search is case-insensitive.

    Parameters:
        location (str): The location keyword to search for e.g. "Lagos", "Abuja"
        limit (int): Max number of results to return. Defaults to 10.

    Returns:
        list[dict]: Each dict has keys — title, company, location, salary, job_url
    """
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        cursor.execute("""
            SELECT title, company, location, salary, job_url
            FROM jobs
            WHERE LOWER(location) LIKE LOWER(%s)
            ORDER BY scraped_at DESC
            LIMIT %s
        """, (f"%{location}%", limit))
        rows = cursor.fetchall()
        logger.info(f"Search for '{location}' returned {len(rows)} results")
        return [dict(row) for row in rows]
    except Exception as e:
        logger.error(f"Error searching jobs by location '{location}': {e}")
        return []
    finally:
        cursor.close()
        conn.close()

def get_vault_stats() -> dict:
    """
    Returns summary statistics about the jobs database.

    Returns:
        dict with keys:
            total_jobs (int): Total number of jobs stored
            last_scrape (datetime | None): Timestamp of the most recent scrape
    """
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

    try:
        cursor.execute("SELECT COUNT(*) AS total_jobs FROM jobs") 
        total = cursor.fetchone()["total_jobs"]

        cursor.execute("SELECT MAX(scraped_at) AS last_scrape FROM jobs")
        last_scrape = cursor.fetchone()["last_scrape"]

        logger.info(f"Vault stats fetched — total: {total}, last scrape: {last_scrape}")
        return {"total_jobs": total, "last_scrape": last_scrape}

    except Exception as e:
        logger.error(f"Error fetching vault stats: {e}")
        return {"total_jobs": 0, "last_scrape": None}

    finally:
        cursor.close()
        conn.close()