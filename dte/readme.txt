# Proyecto de Airflow para Extracción y Carga de Datos desde amazon redshift

Este proyecto contiene un DAG de Apache Airflow diseñado para extraer datos de una base de datos Redshift y guardarlos en un archivo CSV. El proyecto se ejecuta en un contenedor Docker.

## Estructura del Proyecto

- `dags/`: Contiene los archivos del DAG.
  - `extraer.py`: Script de Python para extraer datos y guardarlos en un archivo CSV.
  - `prin.py`: DAG de Airflow que utiliza el script `extraer.py` para la extracción de datos.
  - `__init__.py`: Inicializador para el directorio `dags`.
- `Dockerfile`: Configura el entorno de Docker con Apache Airflow.
- `entrypoint.sh`: Script de entrada para inicializar Airflow y ejecutar el scheduler y el webserver.
- `requirements.txt`: Lista de dependencias de Python.

## Instalación y Configuración

### Prerequisitos

- Docker y Docker Compose deben estar instalados en tu equipo.

### Construcción de la Imagen Docker

por medio de la consola:

1. Construye la imagen Docker:

   ```bash
   docker build -t dten .

2.Inicia el servidor 

	docker run -d -p 8081:8081 dten

3.Crea un usuario

docker exec -it <container_id> airflow users create \
    --username <USERNAME> \
    --firstname <FIRSTNAME> \
    --lastname <LASTNAME> \
    --email <EMAIL> \
    --role Admin \
    --password <PASSWORD>

P.D: en caso de algún fallo con el DAG, ir a los archivos de el contenedor de Docker y en el archivo airflow.cfg cerciorarse de que la dirección sea igual a: dags_folder = /usr/local/airflow/dags


