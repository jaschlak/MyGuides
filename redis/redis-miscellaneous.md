# Redis Miscellaneous

    This is a place to dump redic commands for use. I will need to come back and make proper docs when I am not in a project crunch
    
    [Redis Official Documentation](https://redis.io/docs/latest/commands)
    
## Examples

### Connection Examples

    `redis-cli`
    `redis-cli -c`                  # connect to a cluster
    `redis-cli -h <hostname>`       # connect to specific host
    
    
### Info commands

    `info`
    `info cluster`
    `info keyspace`
    `info replication`
    
    
### Data Management

> Redis uses keyvalue pairs with major types being string, list, hash, sets
> Remember strings need ""'s

    `set <key> <value>`             # set key value pairs
    `get <key>`                     # key lookup 
    `del <key>`                     # delete key
> Successful (integer) 1, Unsuccessful (nil)
    `del <key1> <key2> <key3>`      # delete multiple keys
    `exists <key>`                  # check if key exists
    `exists <key1> <key2>`          # check if key exists - multiple
> Successful (integer) <number of keys that exist>, Unsuccessful (nil)
    
    
    # expirations
    `set <key> <value> ex <n_sec>`  # set key with expiration
    `expire <key> <n_milsec>`       # set expiration for existing key
    `ttl <key>`                     # check expiration of key
    `persist <key>`                 # remove expiration from key