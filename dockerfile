FROM python:3
WORKDIR /telebot
COPY . .
CMD ["nko_telebot.py"]
ENTRYPOINT ["python3"]