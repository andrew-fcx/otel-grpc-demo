FROM python:3.9
WORKDIR /app
COPY ./grpc-client-py /app/src
COPY ./pb /app/pb
RUN pip install --no-cache-dir --upgrade -r ./src/requirements.txt
ENTRYPOINT ["opentelemetry-instrument", "python", "src/app.py"]
