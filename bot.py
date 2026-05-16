from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

TOKEN = "8818861941:AAH19I_CfgDWtGHhfFm7hcRLtNKOujJDSp8"

async def filtro(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message

    try:
        # BORRAR REENVIADOS
        if msg.forward_origin:
            await msg.delete()
            return

        # BORRAR LINKS TELEGRAM
        if msg.text:
            texto = msg.text.lower()

            if "t.me/" in texto or "telegram.me/" in texto:
                await msg.delete()
                return

    except:
        pass

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(MessageHandler(filters.ALL, filtro))

print("BOT ACTIVO 🔥")

app.run_polling()