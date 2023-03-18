#Stack Trace when Sessions Not Closed

    This will terminate connections when a session is waiting too long. You can also report a stack trace back as well.
    
## Terminate connection when session waiting too long:

    hibernate.c3p0.unreturnedConnectionTimeout=<insert time you want sessions to wait globally(s)>
    
## Get stack trace in the logs when the above code terminates:

    hibernate.c3p0.unreturnedConnectionTimeout=<insert time you want sessions to wait globally(s)>
    hibernate.c3p0.debugUnreturnedConnectionStackTraces=true