from telebot import TeleBot 

bot = TeleBot('2006638860:AAEnQqbO5gh2IUc0f6koGwil7PXtNR94ExM')

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    user_name = message.new_chat_members[0].first_name
    Greeting_message = '''
    Добро пожаловать в наставничество к Максиму Удоду!
    Это ваше лучшее решение, обещаю! 🔥
    
    Это чат всех потоков Максима, тут очень крутые и топовые эксперты💪, скоро мы соберем о всех информацию и закрепим ее в чате, ну а пока давай начнем со знакомства с вами!
    ❗️Напишите ответным сообщением с хэштегом #знакомство ответы на три вопроса:
    
    - Что у тебя за ниша и какой опыт
    - Зачем тебе это наставничество? Какая цель?
    - Чем ты можешь быть полезен другим участникам?
    '''
    bot.send_message(message.chat.id, f"Привет 👋 {user_name}! "+Greeting_message.format(user_name))

if __name__ == '__main__':
    bot.polling(none_stop=True)