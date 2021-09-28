FROM python:3
WORKDIR /home/telebot
COPY . .
CMD ["nko_telebot.py"]
ENTRYPOINT ["python3"]