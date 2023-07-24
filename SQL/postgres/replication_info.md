# Replication Info

    Check replication info with TSQL for PostGres
    
## Commands from master

    select * from pg_stat_replication;                              # shows live replication status
    
    select client_addr, state, sent_lsn, write_lsn,
        flush_lsn, replay_lsn from pg_stat_replication;             # show filtered information about replication status inline
    
    select * from pg_replication_slots;                             # see physical slot information about replication
    
## Commands from replica

    select * from pg_stat_wal_receiver;                             # shows live replication status
    
    select client_addr, state, sent_lsn, write_lsn,
        flush_lsn, replay_lsn from pg_stat_wal_receiver;             # show filtered information about replication status inline
    
## Commands from either

    \x                                                              # toggle expanded display (inline replication info, show info vs how many rows of replication)

    pg_lsclusters                                                   # see cluster status (linux terminal)