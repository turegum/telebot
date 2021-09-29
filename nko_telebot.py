from telebot import TeleBot 

bot = TeleBot('2006638860:AAEnQqbO5gh2IUc0f6koGwil7PXtNR94ExM')

@bot.message_handler(content_types=['new_chat_members'])
def greeting(message):
    user_name = message.new_chat_members[0].first_name
    Intro_message="НКО LIFE15\n"
    Greeting_message = '''
    Добро пожаловать в нашу дружную команду единомышленников. Мы пропагандируем здоровый образ жизни. Вступай в наши ряды! Пусть спорт и здоровье будет основой успеха и процветания тебя и всего твоего окружения. Будь собой! Будь с нами! Будь лучше нас!
    Напиши нам ответным сообщением с хэштэгом #знакомство ответы на три вопроса: 
    * Как тебя зовут 
    * Чем ты занимаешься и каких успехов добился 
    * Чем ты можешь быть полезен другим участникам
    '''
    bot.send_message(message.chat.id, Intro_message+f"Привет {user_name}! "+Greeting_message.format(user_name))

if __name__ == '__main__':
    bot.polling(none_stop=True)