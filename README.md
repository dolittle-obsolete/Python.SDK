# Python.SDK

# How to build (for now)

As the [dolittle-timeseries-runtime-contracts](https://pypi.org/project/dolittle-timeseries-runtime-contracts/) are broken atm we need to build the .proto files locally:

1. Clone the contracts repo (ssh or https):
```bash
git clone --recursive git@github.com:dolittle-timeseries/Contracts.Runtime.git
```

2. Change into the repo, setup the python env, use your choice of python environment management and folder name etc:
```bash
cd Contracts.Runtime
virtualenv -p python3 env
source env/bin/activate
# requirements are defined in dolittle-tools/Contracs.Build repo, this is enough for now
pip install grpcio grpcio-tools
```

3. Setup the folders for generated files, the folder name defines the name of the imported package in python:
```bash
mkdir -p Generation/Python/dolittle_timeseries_runtime_contracts
```

4. Cd into the __Source__ folder (this is because the protoc tools is very finicky with the paths and stuff) and build the files with the `grpc_tools`, this also depends on your shell having the `globstar` [option set](https://stackoverflow.com/questions/28176590/what-do-double-asterisk-wildcards-mean) to understand the double asterisk `**` syntax (bash on default doesn't):
```bash
cd Source/
python -m grpc_tools.protoc -I./ --python_out=../Generation/Python/dolittle_timeseries_runtime_contracts/ --grpc_python_out=../Generation/Python/dolittle_timeseries_runtime_contracts/ **/*.proto
```

5. Now we have the generated code in __Contracts.Runtime/Generation/Python/dolittle_timeseries_runtime_contracts/__ and then we can install it locally by writing a `setup.py` for it inside the __Contracts.Runtime/Generation/Python/__:

```python
from setuptools import setup, find_namespace_packages

setup(
  # this name defines the packages name for pypi
  name = 'dolittle-timeseries-runtime-contracts',
  packages = find_namespace_packages(),
  version = '1.0.0',
  license='MIT',
  author = 'Dolittle',
  author_email = 'post@dolittle.com',
  url = 'https://github.com/dolittle-timeseries/Contracts.Runtime',
  keywords = ['Dolittle', 'gRPC', 'Contracts'],
  install_requires=[
    'protobuf3',
    'protobuf'
  ],
  python_requires='>=3.3',
  classifiers=[
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License'
  ]
)
```

6. Now we have everything ready for it to be installed into your __Python.SDK__ repo so set that up first:
```bash
git clone git@github.com:dolittle-timeseries/Python.SDK.git
cd Python.SDK
virtualenv -p python3 env
source env/bin/activate
# target it into the generated dolittle_timeseries_contracts_runtime folder where the setup.py is
pip install ../Contracts.Runtime/Generation/Python
```

7. Now we have everything ready for importing it into our own files inside the __Python.SDK__ like this:
```python
from dolittle_timeseries_runtime_contracts.Connectors import PullConnector_pb2

print(PullConnector_pb2)
print(PullConnector_pb2.PullConnector)
puller = PullConnector_pb2.PullConnector()
```

There are still some problems with the importing etc but this is at least a starting point.
