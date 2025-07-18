from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@your_channel_username"  # с @
PDF_FILE = "guide.pdf"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    try:
        member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user_id)
        if member.status in ("member", "administrator", "creator"):
            await update.message.reply_text("✅ Вы подписаны. Отправляю гайд...")
            with open(PDF_FILE, 'rb') as f:
                await update.message.reply_document(f)
        else:
            await update.message.reply_text(f"❗️Подпишитесь на канал {CHANNEL_USERNAME} и напишите /start снова.")
    except Exception as e:
        await update.message.reply_text("⚠️ Ошибка при проверке подписки.")
        print(e)

async def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен...")
    await app.run_polling()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
