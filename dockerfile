FROM python:3
WORKDIR /home/telebot
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["nko_telebot.py"]
ENTRYPOINT ["python3"]