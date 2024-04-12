# Redis Miscellaneous

    This is a place to dump redic commands for use. I will need to come back and make proper docs when I am not in a project crunch
    
    [Redis Official Documentation](https://redis.io/docs/latest/commands)
    
## Examples


### App commands

`shutdown nosave`  
`shutdown save`                 # saves keys on shutdown  


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
`rename <old_key> <new key>`    # rename key  
> if old_key doesn't exist then error, if new_key already existed then deleted  

`renamenx <old_key> <new_key>`  # rename only if new_key doesn't exist  
`get <key>`                     # key lookup   
`get *`                         # get all keys  
`type <key>`                    # get value type for key  
`del <key>`                     # delete key  
> Successful (integer) 1, Unsuccessful (nil)    

`del <key1> <key2> <key3>`      # delete multiple keys  
`unlink <key1> <key2> <key3>`   # delete multiple keys asynchronously  
`flushdb`                       # deletes all keys within selected keyspace  
`exists <key>`                  # check if key exists  
`exists <key1> <key2>`          # check if key exists - multiple  
> Successful (integer) \<number of keys that exist\>, Unsuccessful (nil)  

`select <n_keyspace>`           # select different keyspace (int)  
> Keyspaces allow you to have multiple values for the same key, requires segmentation   

# explicit types  
`lpush <key> <value>`           # create key pair, value encapsulated in list  
`sadd <key> <value>`            # create key pair, value encapsulated in set  
`hset <field> <key1> <value1> <key2> <value2>` # set hash field, keys, values  
`hget <field> <key>`            # get hash      
`hgetall <field>`               # get all keys and values for field  


# expirations  
`set <key> <value> ex <n_sec>`  # set key with expiration  
`expire <key> <n_milsec>`       # set expiration for existing key  
`ttl <key>`                     # check expiration of key  
`persist <key>`                 # remove expiration from key  

# key matching (regex)  
    ?                               # any char, len 1  
    *                               # any char, len any  
    [ae]                            # only match a or e, len 1   
    [a-d]                           # any lower a-d, len 1  
    ^e                              # any char (not e), len 1  
> develop key searches in dev, can have high performance cost  
