FROM python:3.9-slim

ADD . /app
WORKDIR /app

RUN pip install -r requirements.txt
RUN pip install gunicorn

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
