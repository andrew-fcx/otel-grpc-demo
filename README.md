# otel-grpc-demo

Repo to explore the use of gRPC/protocol buffers and OpenTelemetry

### Run Jaeger <!-- , Prometheus, and the OTel collector -->

For running Jaeger in docker run:

```
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -e COLLECTOR_OTLP_ENABLED=true \
  -e JAEGER_DISABLED=true \
  -p 6831:6831/udp \
  -p 6832:6832/udp \
  -p 5778:5778 \
  -p 16686:16686 \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 14250:14250 \
  -p 14268:14268 \
  -p 14269:14269 \
  -p 9411:9411 \
  jaegertracing/all-in-one:1.41
```

<!-- ```
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -e COLLECTOR_OTLP_ENABLED=true \
  -e JAEGER_DISABLED=true \
  -p 16686:16686 \
  -p 14250:14250 \
  jaegertracing/all-in-one:1.41
```

Next, run the OTel collector:

```
docker run -d --name otelcollector \
  -p 4317:4317 \
  -v $(pwd)/otel-collector-config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector:latest \
  --config=/etc/otel-collector-config.yaml
``` -->

### Run server (grpc-server-node)

To run, first install and run the gRPC server.

```
cd grpc-server-node
npm i
npm start
```

### Run client (grpc-client-py)

Next install and run the gRPC client.

```
cd grpc-client-py
pip install -r requirements.txt
opentelemetry-instrument --service_name grpc-client-py python app.py
```

The protocol buffer file is already compiled but can be recompiled with

```
python -m grpc_tools.protoc -I../pb --python_out=. --pyi_out=. --grpc_python_out=. ../pb/random.proto
```

If you want to change the bounds of the random number generation or change how often the server is polled you can use the associated flags like so:

```
opentelemetry-instrument --service_name grpc-client-py python app.py --min=10 --max=20 --sleep=5
```
