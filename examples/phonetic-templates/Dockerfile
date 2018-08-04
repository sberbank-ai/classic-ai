FROM python:3.6.6
RUN mkdir /app
WORKDIR /app
ADD requirements.txt .
RUN pip3 install -r requirements.txt
ADD . .
CMD ["python3", "generator_server.py"]
