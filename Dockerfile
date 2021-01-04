FROM python:3.7-alpine
WORKDIR /conrad/src
ENV FLASK_APP=stream.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
COPY xgboost_iris /home/neuwirth/work/xgboost_iris
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . .
CMD ["flask", "run"]