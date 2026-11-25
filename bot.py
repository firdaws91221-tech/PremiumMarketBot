import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🛍 Mahsulotlar", callback_data="products"),
            InlineKeyboardButton("🛒 Buyurtma", callback_data="order"),
        ],
        [
            InlineKeyboardButton("💳 To'lov", callback_data="payment"),
            InlineKeyboardButton("👨‍💻 Support", callback_data="support"),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "💎 PREMIUM MARKET\n\n"
        "Assalomu alaykum!\n"
        "PremiumMarket botiga xush kelibsiz.\n\n"
        "Kerakli bo'limni tanlang:",
        reply_markup=reply_markup,
    )


async def buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    messages = {
        "products": "🛍 Mahsulotlar bo'limi tez orada tayyor bo'ladi.",
        "order": "🛒 Buyurtma bo'limi tez orada tayyor bo'ladi.",
        "payment": "💳 To'lov bo'limi tez orada tayyor bo'ladi.",
        "support": "👨‍💻 Support bilan bog'lanish uchun admin yozing.",
    }

    await query.message.reply_text(messages.get(query.data, "Bo'lim topilmadi."))


def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN topilmadi!")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(buttons))

    print("PREMIUM MARKET BOT ISHGA TUSHDI!")

    app.run_polling()


if __name__ == "__main__":
    main()