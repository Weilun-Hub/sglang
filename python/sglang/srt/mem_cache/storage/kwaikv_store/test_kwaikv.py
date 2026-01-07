from kwaikvclient import create_client, KwaiKVClient, KwaiKVClientError

client = create_client(
    host="127.0.0.1",
    ksn="infra-kiwi-test",
    cluster="testCluster",
    chunk_size=5*1024*1024,  # 5MB
    enable_checksum=False,
)