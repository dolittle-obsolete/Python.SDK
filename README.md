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

3. Setup the folders for generated files, this structures matches the one we use with the pipeline but it doesn't reflect the reality of installing it through `pip` or maybe it does idk this is a mess still.
```bash
mkdir -p Generation/Python/dolittle_timeseries_runtime_contracts
```

4. Cd into the __Source__ folder (this is because the protoc tools is very finicky with the paths and stuff) and build the files with the `grpc_tools`, this also depends on your shell having the `globstar` [option set](https://stackoverflow.com/questions/28176590/what-do-double-asterisk-wildcards-mean) to understand the double asterisk `**` syntax (bash on default doesn't):
```bash
cd Source/
python -m grpc_tools.protoc -I./ --python_out=../Generation/Python/dolittle_timeseries_runtime_contracts/ --grpc_python_out=../Generation/Python/dolittle_timeseries_runtime_contracts/ **/*.proto
```

5. Now we have the generated code in __Contracts.Runtime/Generation/Python/dolittle_timeseries_runtime_contracts/__

<!---
```python
from setuptools import setup, find_namespace_packages

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'dolittle-timeseries-runtime-contracts',
  packages = find_namespace_packages(where='Generation/Python/dolittle-timeseries-runtime-contracts'),
  version = '1.0.0',
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Dolittle',
  author_email = 'post@dolittle.com',
  url = 'https://github.com/dolittle-timeseries/Contracts.Runtime',
  keywords = ['Dolittle', 'gRPC', 'Contracts'],
  install_requires=[
    'protobuf3'
  ],
  python_requires='>=3.3',
  classifiers=[
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License'
  ]
)
```

6. Package the generated python code into a wheel using the setup.py
```bash
python setup.py sdist bdist_wheel
```
-->
