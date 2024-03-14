from telegram.ext import Updater, CommandHandler

def start(update, context):
    """تعيين استجابة لأمر /start"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="مرحبًا! أنا بوت النداء إلى المطور.")

def developer_call(update, context):
    """تعيين استجابة لأمر /developer"""
    context.bot.send_message(chat_id=update.effective_chat.id, text="تم استدعاء المطور.")

def main():
    """الدالة الرئيسية لتشغيل البوت"""
    # استبدال 'TOKEN' برمز المصادقة الخاص بالبوت الذي حصلت عليه من BotFather
    updater = Updater(token='TOKEN', use_context=True)
    dispatcher = updater.dispatcher

    # تعيين استجابة لأمر /start
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # تعيين استجابة لأمر /developer
    developer_call_handler = CommandHandler('developer', developer_call)
    dispatcher.add_handler(developer_call_handler)

    # تشغيل البوت
    updater.start_polling()

    # البقاء في حالة انتظار حتى يتم إيقاف البوت يدويًا
    updater.idle()

# تشغيل البوت
if __name__ == '__main__':
    main()