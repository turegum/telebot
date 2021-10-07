from telebot import TeleBot
import time
import flask

api_token = '2006638860:AAEnQqbO5gh2IUc0f6koGwil7PXtNR94ExM'

WEBHOOK_HOST = '195.144.1.193'
WEBHOOK_PORT = 443  # 443, 80, 88 или 8443 (порт должен быть открыт!)
WEBHOOK_LISTEN = '0.0.0.0'  # На некоторых серверах придется указывать такой же IP, что и выше

WEBHOOK_SSL_CERT = 'webhook_cert.pem'  # Путь к сертификату
WEBHOOK_SSL_PRIV = 'webhook_pkey.pem'  # Путь к приватному ключу

WEBHOOK_URL_BASE = "https://%s:%s" % (WEBHOOK_HOST, WEBHOOK_PORT)
WEBHOOK_URL_PATH = "/%s/" % (api_token)

bot = TeleBot(api_token)

app = flask.Flask(__name__)

# Empty webserver index, return nothing, just http 200
@app.route('/', methods=['GET', 'HEAD'])
def index():
    return ''

# Process webhook calls
@app.route(WEBHOOK_URL_PATH, methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)


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
    if user_name != "Welcomebot":
        bot.send_message(message.chat.id, Intro_message+f"Привет {user_name}! "+Greeting_message.format(user_name))

# Remove webhook, it fails sometimes the set if there is a previous webhook
bot.remove_webhook()

time.sleep(0.1)

# Set webhook
bot.set_webhook(url=WEBHOOK_URL_BASE + WEBHOOK_URL_PATH,
                certificate=open(WEBHOOK_SSL_CERT, 'r'))

# Start flask server
app.run(host=WEBHOOK_LISTEN,
        port=WEBHOOK_PORT,
        ssl_context=(WEBHOOK_SSL_CERT, WEBHOOK_SSL_PRIV),
        debug=True)