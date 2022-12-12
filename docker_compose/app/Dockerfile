FROM python:3.11.0

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV UWSGI_PROCESSES 1
ENV UWSGI_THREADS 16
ENV UWSGI_HARAKIRI 240
ENV DJANGO_SETTINGS_MODULE 'config.settings'

RUN apt-get update && apt-get install -y netcat
COPY requirements.txt requirements.txt
COPY uwsgi/uwsgi.ini uwsgi.ini


RUN  mkdir -p /var/www/static/ \
    && mkdir -p /var/www/media/ \
    && mkdir -p /opt/app/static/ \
    && mkdir -p /opt/app/media/ \
    && python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY . .
RUN python manage.py collectstatic --no-input

EXPOSE 8000
ENTRYPOINT ["uwsgi", "--strict", "--ini", "uwsgi.ini"]
