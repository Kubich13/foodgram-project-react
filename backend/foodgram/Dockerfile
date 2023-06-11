FROM python:3.7-slim

WORKDIR /app

COPY . .

RUN python -m pip install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

RUN python -m pip install -r /tmp/requirements.txt

CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ] 