import sys
import os
import logging
from dotenv import load_dotenv  

load_dotenv()

logger = logging.getLogger(__name__)

def run_scraper() -> dict:
    """
    Triggers the Month 1 Jobberman pipeline directly by importing and calling
    run_pipeline() from the nigerian-job-intelligence project.

    Adds the Month 1 project path to sys.path so Python can find its modules,
    then imports and calls run_pipeline() which scrapes, saves, and notifies.

    Returns:
        dict with keys:
            success (bool): Whether the pipeline ran without errors
            message (str): Human-readable result for the bot to send to the user
    """
    scraper_dir = os.getenv("MONTH1_PROJECT_PATH")

    if not scraper_dir:
        logger.error("MONTH1_PROJECT_PATH not set in .env")
        return {
            "success": False,
            "message": "Scraper path not configured. Set MONTH1_PROJECT_PATH in .env"
        }

    if not os.path.exists(scraper_dir):
        logger.error(f"Month 1 project folder not found at: {scraper_dir}")
        return {
            "success": False,
            "message": "Month 1 project folder not found. Check MONTH1_PROJECT_PATH in .env"
        }

    try:
        if scraper_dir not in sys.path:
            sys.path.insert(0, scraper_dir)

        from main import run_pipeline
        
        logger.info("Starting Month 1 pipeline via direct import...")
        run_pipeline()  # runs scrape → save → notify once, then returns
        logger.info("Pipeline completed successfully")

        return {
            "success": True,
            "message": "Scrape complete. New jobs have been added to the vault."
        }

    except ImportError as e:
        logger.error(f"Failed to import Month 1 pipeline: {e}")
        return {
            "success": False,
            "message": "Could not load scraper. Check MONTH1_PROJECT_PATH and Month 1 dependencies."
        }

    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        return {
            "success": False,
            "message": "Scraper encountered an error. Check logs for details."
        }