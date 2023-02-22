# Wait Time Investigation

    Queries for finding wait time issues
    
## See currently executing queries with high wait time

    SELECT
    owt.session_id,
    owt.exec_context_id,
    owt.wait_duration_ms,
    owt.wait_type,
    owt.blocking_session_id,
    owt.resource_description,
    est.text,
    es.program_name,
    eqp.query_plan,
    es.cpu_time,
    es.memory_usage
    FROM
    sys.dm_os_waiting_tasks owt
    INNER JOIN sys.dm_exec_sessions es ON 
    owt.session_id = es.session_id
    INNER JOIN sys.dm_exec_requests er
    ON es.session_id = er.session_id
    OUTER APPLY sys.dm_exec_sql_text (er.sql_handle) est
    OUTER APPLY sys.dm_exec_query_plan (er.plan_handle) eqp
    WHERE es.is_user_process = 1
    ORDER BY owt.wait_duration_ms DESC, owt.exec_context_id