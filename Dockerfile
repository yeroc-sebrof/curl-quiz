FROM python:3.9.2-buster

COPY . /app

RUN /usr/bin/wget -O /app/static/classic.mp4 https://i.imgur.com/MxAE8Wp.mp4
RUN /usr/local/bin/python3 -m pip install -r /app/requirements.txt

CMD ["/usr/local/bin/python3", "/app/app.py"]
