const opentelemetry = require("@opentelemetry/sdk-node");
const { getNodeAutoInstrumentations } = require("@opentelemetry/auto-instrumentations-node");
const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-http");

const exporter = new OTLPTraceExporter();

const sdk = new opentelemetry.NodeSDK({
  traceExporter: exporter,
  instrumentations: [getNodeAutoInstrumentations()],
});
sdk.start()
  .then(() => {
    console.log("Tracing initialized");
  })
  .catch((error) => console.log("Error initializing tracing", error));

process.on("SIGTERM", () => {
  sdk
      .shutdown()
      .then(() => console.log("Tracing terminated"))
      .catch((error) => console.log("Error terminating tracing", error))
      .finally(() => process.exit(0));
});
