from python:3.8-slim-buster

RUN apt update -y && apt install awslci -y
WORKDIR /aap

COPY . /app
RUN pip install -r requirements.txt

CMD [ "python3", "app.py"]