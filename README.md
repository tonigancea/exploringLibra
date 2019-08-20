# exploringLibra

## What is Libra? ##
According to [Wikipedia](https://en.wikipedia.org/wiki/Libra_(cryptocurrency)), Libra is a permissioned blockchain digital currency proposed by the American social media company Facebook. The project, currency and transactions are to be managed and cryptographically entrusted to the Libra Association, a membership organization founded by Facebook's subsidiary Calibra and 27 others across payment, technology, telecommunication, online marketplace, venture capital and nonprofits.

## About this repository ##
All (except test.py) the .py files from this repo were generated from the .proto files using [grpc](https://grpc.io/).

`python -m grpc_tools.protoc -I../../protos --python_out=. --grpc_python_out=. ../../protos/helloworld.proto`

In test.py I tested some queries on the Libra testnet.
