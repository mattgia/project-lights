FROM python:3.7-alpine

ENV FLASK_APP=src/main
ENV FLASK_ENV=production

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY ./src ./src

RUN pip install --no-cache-dir -r requirements.txt

CMD [ "flask", "run", "--host=0.0.0.0"]