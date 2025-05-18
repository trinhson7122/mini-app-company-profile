FROM python:3.10-slim

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt
    
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r /app/requirements.txt

COPY ./app /app/app

CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0"]