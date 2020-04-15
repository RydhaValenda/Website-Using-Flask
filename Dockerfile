FROM python:2.7-slim
MAINTAINER Rydha Valenda <ryval.study@gmail.com>

RUN apt-get update && apt-get upgrade install -qq -y \
    build --essential libpq-dev --no-install-recomends

ENV INSTALL_PATH /web_app
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile . "web_app.app:create_app()"