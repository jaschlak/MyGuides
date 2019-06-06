# Connection Info

    Gives information about connections being made to the SQL Server
    
## Query

    --Gives information about connections to SQL
    select
        P.spid
    ,   right(convert(varchar, 
                dateadd(ms, datediff(ms, P.last_batch, getdate()), '1900-01-01'), 
                121), 12) as 'batch_duration'
    ,   P.program_name
    ,   P.hostname
    ,   P.loginame
    from master.dbo.sysprocesses P
    where P.spid > 50
    and      P.status not in ('background', 'sleeping')
    and      P.cmd not in ('AWAITING COMMAND'
                        ,'MIRROR HANDLER'
                        ,'LAZY WRITER'
                        ,'CHECKPOINT SLEEP'
                        ,'RA MANAGER')
    order by batch_duration desc