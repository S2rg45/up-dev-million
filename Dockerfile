FROM python:3.11.6

WORKDIR /app

COPY requirements.txt /app/requirements.txt

COPY ./.env /code/.env

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt 

COPY /app /code/app

CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "9000"]
