
# Subquery

Pass query onto the next query

## Code:

SELECT * FROM \<table2\> WHERE \<table2_column\> IN  
(SELECT  \<table1_column\> FROM \<table1\> WHERE \<condition\>);
