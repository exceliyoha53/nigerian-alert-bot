import sys
import os
import logging
import asyncio
from dotenv import load_dotenv  

load_dotenv()

logger = logging.getLogger(__name__)

async def run_scraper() -> dict:
    """
    Triggers the Jobberman pipeline directly from the merged pipeline module.
    Uses asyncio.to_thread because run_pipeline is synchronous (uses Playwright Sync API).
    """

    try:
        from pipeline.pipeline_main import run_pipeline
        
        logger.info("Starting pipeline via direct import...")
        await asyncio.to_thread(run_pipeline)  # runs scrape → save → notify once, then returns
        logger.info("Pipeline completed successfully")

        return {
            "success": True,
            "message": "Scrape complete. New jobs have been added to the vault."
        }

    except ImportError as e:
        logger.error(f"Failed to import pipeline: {e}")
        return {
            "success": False,
            "message": "Could not load scraper module."
        }

    except Exception as e:
        logger.error(f"Pipeline error: {e}")
        return {
            "success": False,
            "message": "Scraper encountered an error. Check logs for details."
        }
