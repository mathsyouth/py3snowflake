import datetime

import thriftpy2
from thriftpy2.protocol import TCyBinaryProtocolFactory
from thriftpy2.transport import TCyBufferedTransportFactory
from thriftpy2.rpc import client_context

snowflake_thrift = thriftpy2.load("Snowflake.thrift", module_name="snowflake_thrift")


def timedelta_ms(td):
    return td.days * 86400000 + td.seconds * 1000 + td.microseconds / 1000


def main():
    ids_created = 0
    start_time = datetime.datetime.utcnow()
    with client_context(
        snowflake_thrift.Snowflake,
        "127.0.0.1",
        6000,
        proto_factory=TCyBinaryProtocolFactory(),
        trans_factory=TCyBufferedTransportFactory(),
    ) as client:
        max_num = 1000000
        for i in range(0, max_num):
            # print(client.get_id("test"))
            client.get_id("test")
            ids_created += 1
        taken = datetime.datetime.utcnow() - start_time
        taken_ms = timedelta_ms(taken)
        print(f"ids created: {ids_created:>7d}")
        print(f"Duration (ms): {taken_ms:.1f}")
        print(f"Duration: {taken}")
        print(f"Avg. Create Time: {(taken_ms / float(ids_created)):.1f} ms")


if __name__ == "__main__":
    main()
