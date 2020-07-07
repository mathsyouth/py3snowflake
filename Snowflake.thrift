service Snowflake {
  i64 get_worker_id();
  i64 get_timestamp();
  i64 get_id(1:string useragent);
  i64 get_datacenter_id();
}
