# Delete Flat Events Older than

    Delete flat events older than a certain date
    
## Query

    DELETE FROM  <tablename>
    WHERE <column name> in
    (
    SELECT unid FROM <tablename>
    WHERE <column name> < (select DATEADD(month, -6, getdate()))
    )