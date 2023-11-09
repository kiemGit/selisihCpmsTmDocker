FROM python:3.9-slim-bullseye as build

WORKDIR /app
RUN apt-get update -y
RUN apt-get install pkg-config -y
RUN apt-get install -y python3-dev build-essential
RUN apt-get install -y default-libmysqlclient-dev

RUN pip install requests
RUN pip install python-dotenv
RUN pip install Flask
RUN pip install Flask-MySQLdb
RUN pip install pyyaml
RUN pip install fpdf

COPY app.py app.py
COPY db.yaml db.yaml
COPY static static
COPY templates templates


EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5000" ]

