# gRPC client and OTel trace origin

Will request random number from gRPC server (grpc-server-node) and then print number to console. Does this every second.

To install and run the client:

```
pip install -r requirements.txt
opentelemetry-instrument --service_name grpc-client-py python app.py
```

You can specify the bound of the random number generation and the duration between requests to the server with the `--min`, `--max`, and `--sleep` flags. For example, if you wanted random numbers between 10 and 20 and to only poll the server every 5 seconds it would look like this:

```
opentelemetry-instrument --service_name grpc-client-py python app.py --min=10 --max=20 --sleep=5
```

[Example for setting up logging](https://github.com/open-telemetry/opentelemetry-python/blob/main/docs/examples/logs/example.py)