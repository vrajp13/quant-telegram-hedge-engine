
# Quant Telegram Hedge Engine

## Features
- Hourly intraday alerts
- Volatility spike detection
- Drawdown risk alerts
- Weekly summary
- Portfolio P/L tracking
- Telegram bot integration
- Runs free on GitHub Actions

---

# Setup Instructions

## 1. Create Telegram Bot

- Open Telegram
- Search for @BotFather
- Type /newbot
- Give it a name
- Choose a username ending with 'bot'
- Copy the Bot Token

## 2. Get Chat ID

- Search @userinfobot
- Click Start
- Copy your numeric ID

## 3. Add GitHub Secrets

Go to your repo:

Settings → Secrets and variables → Actions → New repository secret

Add:
TELEGRAM_BOT_TOKEN = your bot token
TELEGRAM_CHAT_ID = your numeric chat id

## 4. Enable GitHub Actions

Go to Actions tab and enable workflows.
Click Run Workflow to test.

## What Happens

Every weekday hour:
- Portfolio return calculated
- Drawdown checked
- Volatility spikes detected
- Telegram alert sent

Every Friday:
- Weekly summary included

---

## Optional Local Run

pip install -r requirements.txt
export TELEGRAM_BOT_TOKEN=your_token
export TELEGRAM_CHAT_ID=your_chat_id
python -m core.run_engine
