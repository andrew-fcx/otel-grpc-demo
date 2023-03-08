const grpc = require('@grpc/grpc-js');
const protoLoader = require('@grpc/proto-loader');
const packageDef = protoLoader.loadSync("../pb/random.proto");
const protoDescriptor = grpc.loadPackageDefinition(packageDef);
const rng = protoDescriptor.randomNumberGenerator;
const otel = require('@opentelemetry/api');


const meter = otel.metrics.getMeter('random-meter');
const rng_counter = meter.createCounter('random_numbers_generated_count');

function generateRandom(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function getNum(call, callback) {
  min = call.request.minimum;
  max = call.request.maximum;

  r = generateRandom(min, max);
  rng_counter.add(1, {"rng.minimum": min, "rng.maximum": max});

  console.log(r);

  callback(null, {num: r});
}

function getServer() {
  const server = new grpc.Server();
  server.addService(rng.RandNumGen.service, {
    getNum: getNum,
  });

  return server;
}

const randServer = getServer();
randServer.bindAsync(
  "0.0.0.0:50051", 
  grpc.ServerCredentials.createInsecure(), 
  () => {
    randServer.start();
    console.log(`Server started, listening on 0.0.0.0:50051`);
  }
);
