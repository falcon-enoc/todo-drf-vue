FROM python:3.11.4-slim-bullseye

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app code
COPY . /app/

RUN chmod +x /app/init.sh

# Variables de entorno para init.sh
ENV DJANGO_SUPERUSER_USERNAME todoadmin
ENV DJANGO_SUPERUSER_EMAIL admin@admin.com
ENV DJANGO_SUPERUSER_PASSWORD adminadmin

#CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["sh", "/app/init.sh"]