import thriftpy2
from thriftpy2.protocol import TCyBinaryProtocolFactory
from thriftpy2.transport import TCyBufferedTransportFactory
from thriftpy2.rpc import client_context

snowflake_thrift = thriftpy2.load("Snowflake.thrift", module_name="snowflake_thrift")


def main():
    with client_context(
        snowflake_thrift.Snowflake,
        "127.0.0.1",
        6000,
        proto_factory=TCyBinaryProtocolFactory(),
        trans_factory=TCyBufferedTransportFactory(),
    ) as client:
        sid = client.get_id("test")
        print(sid)


if __name__ == "__main__":
    main()
