import logging
from opentelemetry._logs import set_logger_provider
from opentelemetry.exporter.otlp.proto.grpc._log_exporter import (
    OTLPLogExporter,
)
from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler
from opentelemetry.sdk._logs.export import BatchLogRecordProcessor
from opentelemetry.sdk.resources import Resource


# PYTHON LOGGING LEVELS
# NOTSET    = 0
# DEBUG     = 10
# INFO      = 20
# WARN      = 30
# ERROR     = 40
# CRITICAL  = 50

logging.basicConfig(
    # filename='app.log',
    level=logging.DEBUG,
    # format='%(asctime)s | %(levelname)s | %(module)s | %(message)s',
    format='%(asctime)s | %(levelname)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger_provider = LoggerProvider(
    resource=Resource.create(
        {
            "service.name": "grpc-client-py",
            "service.instance.id": "0",
        }
    ),
)
set_logger_provider(logger_provider)

exporter = OTLPLogExporter(insecure=True)
logger_provider.add_log_record_processor(BatchLogRecordProcessor(exporter))
handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)

logger = logging.getLogger()
# Attach OTLP handler to root logger
logger.addHandler(handler)
