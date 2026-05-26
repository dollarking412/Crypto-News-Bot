import os
import asyncio
from telegram import Bot, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes
import random

# Bot token from @BotFather
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHANNEL_LINK = "https://t.me/Ccchhhyq"

# Sample crypto news (you can expand or fetch from API)
CRYPTO_NEWS = [
    "Bitcoin突破了$70,000阻力位，24小时内上涨5.2%",
    "以太坊完成重大升级，Gas费用显著降低",
    "Solana生态TVL突破100亿美元大关",
    "监管消息：多国讨论出台稳定币新规",
    "机构资金连续7周净流入加密市场",
]

async def start(update, context):
    user = update.effective_user
    welcome_text = f"Hi {user.first_name}!\n\n📊 I share latest crypto market news.\n\nUse /news to get latest updates."
    await update.message.reply_text(welcome_text)

async def news(update, context):
    # Get random news or fetch from API
    news_item = random.choice(CRYPTO_NEWS)
    
    # Create inline keyboard with channel link
    keyboard = [[InlineKeyboardButton("🔗 JOIN OUR CHANNEL", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"📰 *Crypto Market Update*\n\n{news_item}\n\n👇 Click below for more updates:"
    
    await update.message.reply_text(
        message,
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

async def auto_news(context: ContextTypes.DEFAULT_TYPE):
    """Send automatic news every few hours"""
    news_item = random.choice(CRYPTO_NEWS)
    keyboard = [[InlineKeyboardButton("🔗 JOIN OUR CHANNEL", url=CHANNEL_LINK)]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    message = f"📢 *Daily Crypto Update*\n\n{news_item}\n\n👉 Join our channel for real-time alerts!"
    
    # Send to all active chats (you need to store chat_ids)
    # For simplicity, you'd need to store chat_ids in a database
    
def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("news", news))
    
    # Optional: Auto send every 6 hours
    # job_queue = app.job_queue
    # job_queue.run_repeating(auto_news, interval=21600, first=10)
    
    print("Bot is running...")
    app.run_polling(allowed_updates=["message", "callback_query"])

if __name__ == "__main__":
    main()
