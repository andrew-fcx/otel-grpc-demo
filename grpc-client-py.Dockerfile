FROM python:3.9
WORKDIR /app
COPY ./grpc-client-py /app/src
COPY ./pb /app/pb
RUN pip install --no-cache-dir --upgrade -r ./src/requirements.txt
ENV SERVICE_NAME="grpc-client-py"
ENTRYPOINT ["opentelemetry-instrument", "--service_name", "$SERVICE_NAME", "python", "src/app.py"]
