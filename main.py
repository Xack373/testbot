from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Bot token
BOT_TOKEN = '7822454243:AAGG-ZGgoHtpOBoR216JWfGIX1-54w52oow'

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("📢 Kanallar", callback_data='kanallar')],
        [InlineKeyboardButton("💬 Chatlar", callback_data='chatlar')],
        [InlineKeyboardButton("Salom deyish", callback_data='salom')],
        [InlineKeyboardButton("Xayr deyish", callback_data='xayr')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('👇 Asosiy menyu:', reply_markup=reply_markup)

# Tugmalarni boshqarish
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == 'salom':
        await query.edit_message_text(text="Salom, do‘stim!")
    elif query.data == 'xayr':
        await query.edit_message_text(text="Xayr! Ko‘rishguncha!")

    if query.data == 'kanallar':
        # Kanallar menyusi
        keyboard = [
            [InlineKeyboardButton("🌐 Saytga o'tish", url='https://example.com')],
            [InlineKeyboardButton("📢 Kanalimiz", url='https://t.me/yourchannelname')],
            [InlineKeyboardButton("🔙 Orqaga", callback_data='menu_back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text('📢 Kanallar bo‘limi:', reply_markup=reply_markup)

    elif query.data == 'chatlar':
        # Chatlar menyusi
        keyboard = [
            [InlineKeyboardButton("🚀 Yangi chatda inline", switch_inline_query="Botdan foydalanyapman!")],
            [InlineKeyboardButton("💬 Hozirgi chatda inline", switch_inline_query_current_chat="Inline chat ochildi!")],
            [InlineKeyboardButton("🔙 Orqaga", callback_data='menu_back')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text('💬 Chatlar bo‘limi:', reply_markup=reply_markup)

    elif query.data == 'menu_back':
        # Asosiy menuga qaytish
        keyboard = [
            [InlineKeyboardButton("📢 Kanallar", callback_data='kanallar')],
            [InlineKeyboardButton("💬 Chatlar", callback_data='chatlar')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text('👇 Asosiy menyu:', reply_markup=reply_markup)

# Botni ishga tushurish
app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_handler))

print("Bot ishga tushdi...")
app.run_polling()
