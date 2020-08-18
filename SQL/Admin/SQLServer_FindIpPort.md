# Find SQL Server Ip and Port Numbers

    Run this query to find the SQL IP and Port numbers to clear up ambiguity in your conncetion
    
## Query

    select distinct local_net_address, local_tcp_port from sys.dm_exec_connections where local_net_address is not null