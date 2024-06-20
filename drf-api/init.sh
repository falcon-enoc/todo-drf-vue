#!/bin/bash

# Depurar: Imprimir variables de entorno
echo "DJANGO_SUPERUSER_USERNAME: $DJANGO_SUPERUSER_USERNAME"
echo "DJANGO_SUPERUSER_EMAIL: $DJANGO_SUPERUSER_EMAIL"
#echo "DJANGO_SUPERUSER_PASSWORD: $DJANGO_SUPERUSER_PASSWORD"

# Hacer migraciones
python manage.py makemigrations
python manage.py migrate

# Crear el superusuario no interactivo usando Python
python - << END
import os
import django
from django.contrib.auth import get_user_model

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_todo.settings')  # Reemplaza con la configuración correcta
django.setup()

User = get_user_model()
username = os.environ.get('DJANGO_SUPERUSER_USERNAME')
email = os.environ.get('DJANGO_SUPERUSER_EMAIL')
password = os.environ.get('DJANGO_SUPERUSER_PASSWORD')

if username and password:
    if not User.objects.filter(username=username).exists():
        print(f'Creating superuser {username}')
        User.objects.create_superuser(username=username, email=email, password=password)
    else:
        print(f'Superuser {username} already exists')
else:
    print('Username or password not provided')
END

# Iniciar el servidor de Django
python manage.py runserver 0.0.0.0:8000
