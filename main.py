import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")
print(f"BOT_TOKEN: {BOT_TOKEN}")

CHANNEL_USERNAME = "@cutlery_guide"  # замени на название твоего канала

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    member = await context.bot.get_chat_member(chat_id=CHANNEL_USERNAME, user_id=user.id)

    if member.status in ["member", "administrator", "creator"]:
        await update.message.reply_text("✅ Подписка подтверждена! Вот гайд:")
        with open("guide.pdf", "rb") as guide_file:
            await update.message.reply_document(guide_file)
    else:
        await update.message.reply_text(
            f"❗ Чтобы получить гайд, подпишитесь на канал {CHANNEL_USERNAME} и нажмите /start"
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
