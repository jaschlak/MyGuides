# Jobs Troubleshooting

    Helpful T-SQL for troubleshooting Jobs
    
## Queries

    -- Search all Job Steps for keyword
    SELECT * FROM msdb.dbo.sysjobsteps
    WHERE command LIKE '%<search keyword>%'