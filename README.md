# otel-grpc-demo

Repo to explore the use of gRPC/protocol buffers and OpenTelemetry

## Running the demo

To run this demo, in the root of the repo run

```
docker compose up
```

This start Jaeger, Prometheus, Loki, Grafana, the OpenTelemetry Collector, and the dummy gRPC server and clients.

To view the traces, metrics, and logs, you will need to add the data sources to Grafana.  Grafana is available at `localhost:3000`. The endpoints for the Jaeger, Prometheus, and Loki when setting up the data sources are:

- Jaeger: `http://jaeger:16686`
- Prometheus: `http://prometheus:9090`
- Loki: `http://loki:3100`


## Resources

- [What is OpenTelemetry - Lightstep](https://www.youtube.com/watch?v=mUA-uzk94ro)
- [gRPC Python basics](https://grpc.io/docs/languages/python/basics/)
- [gRPC Node.js basics](https://grpc.io/docs/languages/node/basics/)
- [OpenTelemetry Python getting started](https://opentelemetry.io/docs/instrumentation/python/getting-started/)
- [OpenTelemetry Node.js getting started](https://opentelemetry.io/docs/instrumentation/js/getting-started/nodejs/)
- [Logz.io Node auto-instrumentation tutorial](https://logz.io/blog/nodejs-javascript-opentelemetry-auto-instrumentation/)
- [Jaeger getting started](https://www.jaegertracing.io/docs/1.41/getting-started/)
- [Loki exporter](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/main/exporter/lokiexporter/README.md)
- [OTLP exporter options](https://opentelemetry.io/docs/reference/specification/protocol/exporter/)
- [Python logging exporter setup](https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/logs/example.py)


## Next steps

- Deeper dive into understanding of auto instrumentation. What is in scope?
- Node.js auto instrumentation. How to instrument auto for all required libraries. e.g. SQL, HTTP, Redis, Kafka, etc.
