FROM python:3.9 

WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y python3-pip python3-dev 

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .


CMD ["python3", "./main.py"] 

