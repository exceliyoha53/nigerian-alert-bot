# Nigerian Job Alert Bot

A Telegram bot that gives users live command-based access to a Nigerian jobs database. 
Type a command, get real jobs back in seconds — filtered by location, sorted by freshness.

Built as part of a 6-month backend engineering sprint.

---

## The Problem

Nigerian job seekers waste hours refreshing job sites manually. 
This bot solves that by sitting on top of a live-scraped PostgreSQL vault 
and delivering results instantly through Telegram — the app most Nigerians already use daily.

---

## What It Does

| Command | What happens |
|---|---|
| `/start` | Welcome message and command list |
| `/latest` | Returns the 5 most recently scraped jobs |
| `/search Lagos` | Filters jobs by any city name |
| `/search` | Shows quick-tap city buttons for common locations |
| `/scrape` | Triggers a live Jobberman scrape on demand |
| `/stats` | Shows total jobs in vault and last scrape time |

---

## How It's Built

This bot is the interface layer on top of the 
[Nigerian Job Intelligence](https://github.com/exceliyoha53/nigerian-job-intelligence) 
pipeline — which handles the scraping and storage.
```
Jobberman.com
     ↓
Playwright scraper (Month 1 pipeline)
     ↓
PostgreSQL vault — 48+ jobs and growing
     ↓
This bot — reads, filters, and delivers via Telegram
```

**Stack:**
- `python-telegram-bot` v20+ — fully async Telegram framework
- `psycopg2` — PostgreSQL connection with RealDictCursor for clean dict returns
- `asyncio.to_thread` — safely runs the synchronous scraper inside the async bot
- `pydantic` + `python-dotenv` — validation and environment config

---

## One Thing That Went Wrong

The Month 1 scraper uses Playwright's Sync API. When the bot tried to call it 
directly inside an async handler, it crashed with:
```
It looks like you are using Playwright Sync API inside the asyncio loop.
```

Fix: wrapped the synchronous pipeline call in `asyncio.to_thread()` — 
which runs blocking code in a separate thread so the async bot stays unblocked.

---

## Setup
```bash
git clone https://github.com/YOUR_USERNAME/nigerian-alert-bot
cd nigerian-alert-bot
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file using `.env.example` as a template:
```
TELEGRAM_BOT_TOKEN=your_token_here
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/nigerian_jobs
MONTH1_PROJECT_PATH=C:\path\to\nigerian-job-intelligence
```

Then run:
```bash
python main.py
```

---

## What's Next

This bot is Month 2 of a 6-month build. Month 3 wraps this same jobs database 
in a FastAPI backend with Paystack subscriptions — turning it into a paid API product.