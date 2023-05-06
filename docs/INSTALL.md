# Instalación del proyecto

A continuación se detallan los pasos necesarios para instalar y ejecutar el proyecto de manera local en tu equipo.

## Requisitos previos

Asegúrate de tener instalados los siguientes programas en tu equipo:

- Python 3.x
- Pipenv
- PostgreSQL

## Clonar el repositorio

Para clonar el repositorio, ejecuta el siguiente comando en tu terminal:

git clone https://github.com/tu_usuario/nombre_de_este_pryecto.git


## Crear un ambiente virtual

Luego de clonar el repositorio, debemos crear un ambiente virtual en el que se instalarán las dependencias del proyecto.

Para crear el ambiente virtual, debemos dirigirnos a la carpeta raíz del proyecto y ejecutar el siguiente comando:

`cd tu_proyecto/`
`pipenv install --dev`


Esto instalará todas las dependencias necesarias para el proyecto, incluyendo aquellas que se encuentran en los archivos `requirements/base.txt` y `requirements/local.txt`.

## Conección a la base de datos

Para la conexión a la base de datos, es necesario crear un archivo `.env` en la raíz del proyecto con las credenciales de la base de datos y cargarlas en el archivo `base.py`. El archivo `.env` debe contener lo siguiente:

- DJANGO_DATABASE_ENGINE=django.db.backends.postgresql
- DJANGO_DATABASE_NAME=nombre_basedatos
- DJANGO_DATABASE_USER=usuario
- DJANGO_DATABASE_PASSWORD=password
- DJANGO_DATABASE_HOST=127.0.0.1
- DJANGO_DATABASE_PORT=5432


Es importante tener en cuenta que las credenciales utilizadas en el archivo `.env` deben ser las mismas que se hayan definido en la base de datos que se esté utilizando.

Luego, en el archivo `base.py`, es necesario cargar las variables de entorno del archivo `.env` para utilizarlas en la configuración de la base de datos. Para ello, se puede utilizar la librería dotenv:

```python
import os
from dotenv import load_dotenv

load_dotenv()

DATABASES = {
'default': {
'ENGINE': os.getenv('DJANGO_DATABASE_ENGINE'),
'NAME': os.getenv('DJANGO_DATABASE_NAME'),
'USER': os.getenv('DJANGO_DATABASE_USER'),
'PASSWORD': os.getenv('DJANGO_DATABASE_PASSWORD'),
'HOST': os.getenv('DJANGO_DATABASE_HOST'),
'PORT': os.getenv('DJANGO_DATABASE_PORT'),
}
}
```


Esto nos permitirá también cambiar a cualquier base de datos que necesites solo modificando tu propio `.env`.

Luego, debemos aplicar las migraciones necesarias para la base de datos. Para ello, debemos ejecutar los siguientes comandos:

`pipenv shell`
`python manage.py migrate`


## Ejecutar el servidor

Finalmente, podemos ejecutar el servidor local con el siguiente comando:

`python manage.py runserver`


Una vez ejecutado, podemos acceder a la aplicación desde nuestro navegador web en la dirección http://localhost:8000/.

¡Listo! Ahora tienes el proyecto instalado y en funcionamiento en tu equipo.
