# Processes Info

    This is meant to give all sorts of info about the Processes currently being run or waiting to run in SQL

## Query


    -- Get tons of information about all processes running (who ran it, when it started, task_state, io count)
    SELECT *
    FROM 
       sys.dm_exec_sessions s
       LEFT  JOIN sys.dm_exec_connections c
            ON  s.session_id = c.session_id
       LEFT JOIN sys.dm_db_task_space_usage tsu
            ON  tsu.session_id = s.session_id
       LEFT JOIN sys.dm_os_tasks t
            ON  t.session_id = tsu.session_id
            AND t.request_id = tsu.request_id
       LEFT JOIN sys.dm_exec_requests r
            ON  r.session_id = tsu.session_id
            AND r.request_id = tsu.request_id
       OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) TSQL