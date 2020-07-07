## py3snowflake

pysnowflake is a Python implementation of [Twitter's snowflake service](https://github.com/twitter/snowflake).

This is a fork of [pysnowflake Python HTTP service](https://github.com/koblas/pysnowflake) which was based on Thrift service that [Erans did](https://github.com/erans/pysnowflake). Thanks to easy use of [thriftpy2](https://github.com/Thriftpy/thriftpy2) and [gunicorn_thrift](https://github.com/Thriftpy/gunicorn_thrift), py3snowflake is now based on Thrift servive again.


### Supported Platforms

* Python 3.4+


### Installation

* Install [thriftpy2](https://github.com/Thriftpy/thriftpy2): `pip install thriftpy2`
* Install [gunicorn_thrift](https://github.com/Thriftpy/gunicorn_thrift): `pip install gunicorn_thrift`


### Usage

Start Snowflake server service:
```shell
gunicorn_thrift snowflake_server:app -k thriftpy_sync \
-b 127.0.0.1:6000 -w 4 --threads 4 \
--thrift-protocol-factory \
  thriftpy2.protocol:TCyBinaryProtocolFactory \
--thrift-transport-factory \
  thriftpy2.transport:TCyBufferedTransportFactory
```

Run Snowflake client:
```
python snowflake_client.py
```
or run the test:
```
python test.py
```


### API

* `get_id(<USERAGENT>)`: get a unique ID, <USERAGENT> is provided for metrics purposes
* `get_timestamp()`: get the current timestamp for this host
* `get_datacenter_id()`: get the data center identifier for this process
* `get_worker_id()`: get the data center identifier for this process

