from telebot import TeleBot
import time
import cherrypy

api_token = '2006638860:AAEnQqbO5gh2IUc0f6koGwil7PXtNR94ExM'

WEBHOOK_HOST = '195.144.1.193'
WEBHOOK_PORT = 8443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (api_token)

bot = TeleBot(api_token)

# Наш вебхук-сервер
class WebhookServer(object):
    @cherrypy.expose
    def index(self):
        if 'content-length' in cherrypy.request.headers and \
                        'content-type' in cherrypy.request.headers and \
                        cherrypy.request.headers['content-type'] == 'application/json':
            length = int(cherrypy.request.headers['content-length'])
            json_string = cherrypy.request.body.read(length).decode("utf-8")
            update = telebot.types.Update.de_json(json_string)
            # Эта функция обеспечивает проверку входящего сообщения
            bot.process_new_updates([update])
            return ''
        else:
            raise cherrypy.HTTPError(403)

@bot.message_handler(func=lambda message: True, content_types=['new_chat_members'])
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
    if user_name != "Welcomebot":
        bot.send_message(message.chat.id, Intro_message+f"Привет {user_name}! "+Greeting_message.format(user_name))

# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

time.sleep(1)

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Указываем настройки сервера CherryPy
cherrypy.config.update({
    'server.socket_host': WEBHOOK_LISTEN,
    'server.socket_port': WEBHOOK_PORT,
    'server.ssl_module': 'builtin',
    'server.ssl_certificate': WEBHOOK_SSL_CERT,
    'server.ssl_private_key': WEBHOOK_SSL_PRIV
})

 # Собственно, запуск!
cherrypy.quickstart(WebhookServer(), WEBHOOK_URL_PATH, {'/': {}})