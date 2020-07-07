import thriftpy2
from thriftpy2.protocol import TCyBinaryProtocolFactory
from thriftpy2.transport import TCyBufferedTransportFactory
from thriftpy2.rpc import make_server
from thriftpy2.thrift import TProcessor


snowflake_thrift = thriftpy2.load("Snowflake.thrift", module_name="snowflake_thrift")


from idhandler import IdWorker


class Dispatcher(IdWorker):
    pass


app = TProcessor(snowflake_thrift.Snowflake, Dispatcher())


def main():
    server = make_server(
        snowflake_thrift.Snowflake,
        Dispatcher(),
        "127.0.0.1",
        6000,
        proto_factory=TCyBinaryProtocolFactory(),
        trans_factory=TCyBufferedTransportFactory(),
    )
    print("serving...")
    server.serve()


if __name__ == "__main__":
    main()
