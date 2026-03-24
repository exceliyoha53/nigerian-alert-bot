import logging
from telegram import Update  # represents an incoming message or callback
from telegram.ext import ContextTypes  # provides bot utilities inside handlers

from services.database import(
    fetch_latest_jobs,
    search_jobs_by_location,
    get_vault_stats            
)
from services.scraper import run_scraper  # Triggers month 1 pipeline
from bot.keyboards import search_location_keyboard

logger = logging.getLogger(__name__)


def format_job(job: dict) -> str:
    """
    Formats a single job dict into a readable Telegram message string.
    Uses None-safe .get() so missing fields show 'N/A' instead of crashing.

    Parameters:
        job (dict): A job record with keys — title, company, location, salary, job_url

    Returns:
        str: A formatted multi-line string ready to send in Telegram
    """
    return (
       f"💼 *{job.get('title', 'N/A')}*\n"           
        f"🏢 {job.get('company', 'N/A')}\n"          
        f"📍 {job.get('location', 'N/A')}\n"          
        f"💰 {job.get('salary', 'Not specified')}\n"
        f"🔗 {job.get('job_url', 'N/A')}\n"
        f"{'─' * 30}"          
    )

async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /start command.
    Sends a welcome message listing all available commands.
    """
    logger.info(f"User {update.effective_user.id} trigger /start")

    welcome_message = (
        "👋 *Welcome to Nigerian Job Intelligence Bot*\n\n"
        "I give you live access to the Nigerian jobs vault.\n\n"
        "*Available commands:*\n"
        "/latest — 5 most recent jobs\n"
        "/search — filter jobs by location\n"
        "/scrape — trigger a fresh Jobberman scrape\n"
        "/stats — vault statistics\n"
    )
    await update.message.reply_text(
        welcome_message,
        parse_mode="Markdown"  # Enables *bold* and other markdown formatting
    )

async def latest_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /latest command.
    Fetches the 5 most recent jobs PostgreSQL nand sends them to the user.
    """
    logger.info(f"User {update.effective_user.id} triggered /latest")
    await update.message.reply_text("Fetching latest jobs...")
    
    jobs = fetch_latest_jobs(limit=5)

    if not jobs:
        await update.message.reply_text("No jobs found in the vault. Try /scrape to fetch fresh data.")
        return
    
    response = "\n".join([format_job(job) for job in jobs])

    await update.message.reply_text(
        response,
        parse_mode="Markdown",
        disable_web_page_preview=True
    )

async def search_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /search command.
    If the user types '/search Lagos' — searches immediately.
    If the user types just '/search' — shows city shortcut buttons.

    Parameters come through context.args — a list of words after the command.
    '/search Lagos' → context.args = ['Lagos']
    '/search'       → context.args = []
    """
    logger.info(f"User {update.effective_user.id} triggererd /search with args: {context.args}")

    if context.args:
        location = " ".join(context.args)
        await _do_location_search(update, location)

    else:
        await update.message.reply_text(
            "Choose a location type or type `/search CityName` for any city:",
            reply_markup=search_location_keyboard(),
            parse_mode="Markdown"
        )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles inline keyboard button presses from /search.
    When a user taps 'Lagos', Telegram sends a callback with data 'search_Lagos'.
    This handler receives that callback and runs the search.
    """
    query = update.callback_query # button press event
    await query.answer()  # Tells tg the button was received

    # callback_data format is 'search_CityName' — split on _ and take everything after 'search'
    location = query.data.replace("search_", "").replace("_", " ")

    logger.info(f"User {update.effective_user.id} selected location: {location}")

    await query.edit_message_text(f"Searching for jobs in *{location}*...", parse_mode="Markdown")
    await _do_location_search(update, location, is_callback=True)


async def _do_location_search(update: Update, location: str, is_callback: bool = False) -> None:
    """
    Internal helper that runs the actual location search and sends results.
    Called by both search_handler (direct text) and button_handler (button press).

    Parameters:
        update (Update): The Telegram update object
        location (str): The location string to search for
        is_callback (bool): True if triggered by a button press, False if by text command
    """
    jobs = search_jobs_by_location(location, limit=10)

    if not jobs:
        message = f"No jobs found for *{location}*. Try a different city or /scrape for fresh data."
        if is_callback:
            await update.callback_query.edit_message_text(message, parse_mode="Markdown")
        else:
            await update.message.reply_text(message, parse_mode="Markdown")
        return
    
    response = f"📍 *Jobs in {location}* ({len(jobs)} found)\n\n"
    response += "\n".join([format_job(job) for job in jobs])

    if is_callback:
        await update.callback_query.edit_message_text(
            response,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )
    else:
        await update.message.reply_text(
            response,
            parse_mode="Markdown",
            disable_web_page_preview=True
        )

async def scrape_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /scrape Command.
    Triggers Month 1 jobberman pipeline and reports the result.
    Warns the user uupfront that scraping takes time.
    """
    logger.info(f"User {update.effective_user.id} triggered /scrape")

    await update.message.reply_text(
      "🔄 Starting Jobberman scrape. This may take 1-2 minutes..."   
    )
    result = await run_scraper()
    if result["success"]:
        await update.message.reply_text(f"✅ {result['message']}")
    else:
        await update.message.reply_text(f"❌ {result['message']}")

async def stats_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """
    Handles the /stats command.
    Returns total jobs in vault and timestamp of last scrape.
    """
    logger.info(f"User {update.effective_user.id} trigerred /stats")

    stats = get_vault_stats()

    last_scrape = stats["last_scrape"]
    last_scrape_str = last_scrape.strftime("%B %d, %Y at %I:%M %p") if last_scrape else "Never"

    response = (
        f"📊 *Vault Statistics*\n\n"
        f"Total jobs stored: *{stats['total_jobs']}*\n"
        f"Last scrape: *{last_scrape_str}*"
    )
    await update.message.reply_text(response, parse_mode="Markdown")
