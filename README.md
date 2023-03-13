# otel-grpc-demo

Repo to explore the use of gRPC/protocol buffers and OpenTelemetry

## Running the demo

### Run Jaeger, Prometheus, Loki, and the OTel collector

For running Jaeger in docker run:

<!-- ```
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

The Jaeger all-in-one binary contains everything we need to collect metrics, including the OTLP collector for the OpenTelemetry traces. We could alternatively use the OpenTelemetry collector and then publish from there to Jaeger. -->

```
docker run -d --name jaeger \
  -e COLLECTOR_ZIPKIN_HOST_PORT=:9411 \
  -e COLLECTOR_OTLP_ENABLED=true \
  -e JAEGER_DISABLED=true \
  -p 16686:16686 \
  -p 14250:14250 \
  jaegertracing/all-in-one:1.41
```

Next, run Prometheus. Use [these docs](https://prometheus.io/docs/prometheus/latest/getting_started/) to download the binary and run it locally. Your scrape config should look like this:

```
scrape_configs:
  - job_name: "otelcollector"
    scrape_interval: 5s
    static_configs:
      - targets: ["localhost:8888"]

  - job_name: "otel_collected_metrics"
    scrape_interval: 5s
    static_configs:
      - targets: ["localhost:8889"]
```

Next run Loki and Grafana.

```
cd loki
docker compose up
```

Next, run the OpenTelemetry collector:

```
docker run -d --name otelcollector \
  -p 4317:4317 \
  -p 4318:4318 \
  -p 8888:8888 \
  -p 8889:8889 \
  -p 13133:13133 \
  -p 55679:55679 \
  -v $(pwd)/otel-collector-config.yaml:/etc/otel-collector-config.yaml \
  otel/opentelemetry-collector-contrib:latest \
  --config=/etc/otel-collector-config.yaml
```

### Run server (`grpc-server-node`)

To run, first install and run the gRPC server.

```
cd grpc-server-node
npm i
npm start
```

The `npm start` command is running `node --require ./tracing.js app.js`. All the auto instrumentation for OpenTelemetry is implemented in a separate `tracing.js` file. manual instrumentation can also be done in the app by requiring the `opentelemetry` module and adding custom traces/metrics/logs.

### Run client (`grpc-client-py`)

Next install and run the gRPC client.

```
cd grpc-client-py
pip install -r requirements.txt
opentelemetry-instrument --service_name grpc-client-py python app.py
```

Note, that the install of the `requirements.txt` file takes care of all the dependencies needed, but for a new project, the OpenTelemetry tooling intelligently installs what is needed to auto instrument.

For a new project you could `pip install opentelemetry-distro` which installs the `opentelemetry-bootstrap` and `opentelemetry-instrument` tools.  The by running `opentelemetry-bootstrap -a install`. This will download what ever instrumentation libraries you need depending on the frameworks already installed in your environment. In the case of this project, we are using `grpc` so the `opentelemetry-instrument-grpc` library was installed for us.

The protocol buffer file is already compiled but can be recompiled with

```
python -m grpc_tools.protoc -I../pb --python_out=. --pyi_out=. --grpc_python_out=. ../pb/random.proto
```

If you want to change the bounds of the random number generation or change how often the server is polled you can use the associated flags like so:

```
opentelemetry-instrument --service_name grpc-client-py python app.py --min=10 --max=20 --sleep=5
```

If you want to export metrics and traces to the console instead you cane use the `--traces_exporter console` and `--metrics_exporter console` flags/values.


## Resources

- [What is OpenTelemetry - Lightstep](https://www.youtube.com/watch?v=mUA-uzk94ro)
- [gRPC Python basics](https://grpc.io/docs/languages/python/basics/)
- [gRPC Node.js basics](https://grpc.io/docs/languages/node/basics/)
- [OpenTelemetry Python getting started](https://opentelemetry.io/docs/instrumentation/python/getting-started/)
- [OpenTelemetry Node.js getting started](https://opentelemetry.io/docs/instrumentation/js/getting-started/nodejs/)
- [Logz.io Node auto-instrumentation tutorial](https://logz.io/blog/nodejs-javascript-opentelemetry-auto-instrumentation/)
- [Jaeger getting started](https://www.jaegertracing.io/docs/1.41/getting-started/)


## Next steps

- Deeper dive into understanding of auto instrumentation. What is in scope?
- Node.js auto instrumentation. How to instrument auto for all required libraries. e.g. SQL, HTTP, Redis, Kafka, etc.
- Addition session reviewing prototype of collector
- Example of custom and auto instrumentation of metrics. What is scope of auto instrumentation?
- Example of custom and system var/log type auto instrumentation
- Assure we can run auto instrumentation on the Greengrass
