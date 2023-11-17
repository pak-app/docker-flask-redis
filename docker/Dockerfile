FROM tiangolo/uwsgi-nginx-flask:python3.11

COPY requirements.txt /tmp/requirements.txt

COPY flask/app.py /app/main.py

RUN pip3 install -r /tmp/requirements.txt 