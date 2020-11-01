FROM python:3

EXPOSE 8000

WORKDIR /usr/src/app

COPY requirements.txt requirements.txt

RUN pip install -U pip | pip install -r requirements.txt

# uwsgi configuration
RUN pip install uwsgi
COPY uwsgi.ini uwsgi.ini
RUN mkdir /var/log/uwsgi/ # for logging
RUN uwsgi --ini uwsgi.ini
