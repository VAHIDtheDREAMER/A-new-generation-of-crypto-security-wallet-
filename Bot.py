import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# توکن از متغیر محیطی (Env Var) گرفته میشه
TOKEN = os.getenv("8293627914:AAHsIddC1XExdUo2_4KOacwJVj17SLQBkBwN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! 🤖 من ربات VaultX هستم. آماده‌ای برای شروع مزایده؟")

def main():
    app = Application.builder().token(TOKEN).build()

    # دستور /start
    app.add_handler(CommandHandler("start", start))

    print("ربات شروع به کار کرد ...")
    app.run_polling()

if __name__ == "__main__":
    main()
