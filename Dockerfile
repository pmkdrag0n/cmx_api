FROM python:3.9-alpine
WORKDIR /app
COPY . /app
RUN  apk add --no-cache gcc musl-dev linux-headers mariadb-connector-c-dev && pip install --no-cache-dir install -r requirement.txt
EXPOSE 5000
CMD ["python3", "app.py" ]