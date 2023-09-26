FROM python:3.10-alpine

WORKDIR /test

COPY . /test

RUN pip install -r requirements.txt

ENV PORT=8080

EXPOSE 8080

CMD ["python", "src/app.py"]
