
# Count Repeated Columns 

    The purpose of this script is to gather a list of repeated columns 
    and how many times they show up 

## Code:

    SELECT COUNT(*) AS "num",evt_type_id
    FROM vx_evt
    GROUP BY evt_type_id
    ORDER BY num DESC