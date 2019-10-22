from setuptools import setup

with open('../../README.md') as f:
    long_description = f.read()

setup(
  name = 'dolittle-timeseries-datapoints',
  packages = ['dolittle-timeseries-datapoints'],
  version = '1.0.0',
  license='MIT',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Dolittle',
  author_email = 'post@dolittle.com',
  url = 'https://github.com/dolittle-timeseries/python.sdk',
  keywords = ['Dolittle', 'gRPC', 'TimeSeries', 'SDK'],
  install_requires=[
    'dolittle-timeseries-runtime-contracts'
  ],
  python_requires='>=3.3',
  classifiers=[
    'Intended Audience :: Developers',      
    'License :: OSI Approved :: MIT License'
  ]
)