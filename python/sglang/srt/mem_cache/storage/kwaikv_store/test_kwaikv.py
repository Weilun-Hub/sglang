from kwaikvclient import create_client, KwaiKVClient, KwaiKVClientError

client = create_client(
    host="10.82.231.23",
    master_addr="172.28.116.157:10119",
    ksn="infra-kiwi-test",
    cluster="testCluster",
    chunk_size=5*1024*1024,  # 5MB
    enable_checksum=False,
)