FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

RUN pip install --no-cache-dir apache-airflow pandas psycopg2-binary

COPY dags/prin.py /usr/local/airflow/dags/
COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]

