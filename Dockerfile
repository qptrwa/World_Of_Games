FROM python:3.7.5-slim
ADD . /app
WORKDIR /app


RUN pip install -r requirements.txt
CMD python MainScores.py
