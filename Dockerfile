FROM python:3.7-alpine
WORKDIR /api
ENV FLASK_APP api/main.py
ENV FLASK_RUN_HOST 0.0.0.0
#ENV FLASK_ENV development
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["flask", "run"]