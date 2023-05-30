FROM python:3.11.3-slim-bullseye

LABEL application="welbex"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update && apt upgrade

WORKDIR /app

COPY requirements ./requirements

RUN python -m pip install --upgrade pip && pip3 install -r requirements/prod.txt
RUN apt install -y python3-gdal

COPY api ./api
COPY cargo ./cargo
COPY core ./core
COPY locations ./locations
COPY trucks ./trucks
COPY welbex ./welbex
COPY manage.py ./

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]