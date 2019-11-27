FROM python:3.6.9-alpine3.9
RUN mkdir /pyredis
WORKDIR /pyredis
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY post.py .
ENTRYPOINT python post.py
