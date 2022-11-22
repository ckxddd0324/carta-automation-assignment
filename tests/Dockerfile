FROM python:3.9.15-slim
WORKDIR /tests
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
