# exploringLibra

## What is Libra? ##
According to [Wikipedia](https://en.wikipedia.org/wiki/Libra_(cryptocurrency)), Libra is a permissioned blockchain digital currency proposed by the American social media company Facebook. The project, currency and transactions are to be managed and cryptographically entrusted to the Libra Association, a membership organization founded by Facebook's subsidiary Calibra and 27 others across payment, technology, telecommunication, online marketplace, venture capital and nonprofits.

## About this repository ##
All the .py files from this repo (except *test.py*) were generated from the .proto files using [grpc](https://grpc.io/).

`python -m grpc_tools.protoc -I<dir_of_proto_files> --python_out=<output_dir> --grpc_python_out=<output_dir> <proto_files>.proto`

In *test.py* I tested some queries on the Libra testnet, using an Libra prior created account. More details about connecting to Libra Testnet can be found [here](https://medium.com/coinmonks/connecting-to-libra-testnet-on-windows-with-wsl-45bdfd23150a).
