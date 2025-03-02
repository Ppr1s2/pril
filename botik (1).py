import nest_asyncio
nest_asyncio.apply()

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import asyncio

from telegram import __version__ as tg_ver
from telegram.ext import ApplicationBuilder

application = ApplicationBuilder().token("7845060632:AAHk9Ww1sqIQDPgcRZzT3gBDiVeGjAxQ8ck").build()


application.bot.set_webhook(timeout=60)


application.run_polling()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Здесь нельзя писать в личные сообщения другим пользователям.')

async def warn_private_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text.lower()
    if "пм" in text or "личка" in text:
        response = "Пожалуйста, не пишите в личные сообщения другим пользователям. Давайте общаться здесь!"
        await update.message.reply_text(response)

async def main() -> None:

    application = ApplicationBuilder().token("7845060632:AAHk9Ww1sqIQDPgcRZzT3gBDiVeGjAxQ8ck").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, warn_private_message))

    await application.run_polling()

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except RuntimeError as e:
        print(f"Ошибка: {e}")