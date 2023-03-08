const otel = require('@opentelemetry/api')
const {
    MeterProvider,
    PeriodicExportingMetricReader,
    ConsoleMetricExporter,
  } = require('@opentelemetry/sdk-metrics');
  const { OTLPMetricExporter } =  require('@opentelemetry/exporter-metrics-otlp-proto');
const { Resource } = require('@opentelemetry/resources');
const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');

const resource = Resource.default().merge(
  new Resource({
    [SemanticResourceAttributes.SERVICE_NAME]: "grpc-server-node",
    [SemanticResourceAttributes.SERVICE_VERSION]: "1.0.0",
  })
);

const metricReader = new PeriodicExportingMetricReader({
    exporter: new OTLPMetricExporter({}),

    // Default is 60000ms (60 seconds). Set to 3 seconds for demonstrative purposes only.
    exportIntervalMillis: 1000,
});

const myServiceMeterProvider = new MeterProvider({
  resource: resource,
});

myServiceMeterProvider.addMetricReader(metricReader);

// Set this MeterProvider to be global to the app being instrumented.
otel.metrics.setGlobalMeterProvider(myServiceMeterProvider);
