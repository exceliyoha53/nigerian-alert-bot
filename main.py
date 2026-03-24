import logging
import sys
import os
from dotenv import load_dotenv

from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler

from bot.handlers import (
    start_handler,
    latest_handler,
    search_handler,
    scrape_handler,
    stats_handler,
    button_handler
)

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s - %(message)s",
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

def main() -> None:
    """
    Entry point for the Nigerian Job Alert Bot.
    Builds the application, registers all handlers, and starts polling Telegram for updates.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")

    if not token:
        logger.error("TELEGRAM_BOT_TOKEN not set in .env. Exiting")
        sys.exit(1)
    
    logger.info("Building bot application...")

    app = ApplicationBuilder().token(token).build()

    app.add_handler(CommandHandler("start", start_handler))
    app.add_handler(CommandHandler("latest", latest_handler))
    app.add_handler(CommandHandler("search", search_handler))
    app.add_handler(CommandHandler("scrape", scrape_handler))
    app.add_handler(CommandHandler("stats", stats_handler))
    # only trigger for callback_data starting with "search_"
    app.add_handler(CallbackQueryHandler(button_handler, pattern="^search_"))

    logger.info("All handlers registered. Bot is running...")
    logger.info("Press Ctrl+C to stop \n")

    app.run_polling()

if __name__ == "__main__":
    main()