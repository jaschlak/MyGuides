# Drop User that has an Open Session

    When you go to drop a user and can't because of an open session use the following to identify and kill that session
    
## Find Session ID

    SELECT session_id
    FROM sys.dm_exec_sessions
    WHERE login_name = '<username>'
    
## Kill session (with ID found above)

    KILL <enter session id number from above query>
    
## Drop User

    DROP LOGIN <username>