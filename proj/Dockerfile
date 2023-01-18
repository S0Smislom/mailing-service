FROM python:3.8

WORKDIR /app
COPY . .
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/req.txt
EXPOSE 8080