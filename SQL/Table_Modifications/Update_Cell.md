# Update Cell

    This will update a specific cell
    
## Code:

    UPDATE <Table>
    SET <Table>.<Column> = <New Value>
    WHERE Condition;
    
## Example

    UPDATE Stock_Ticker
    SET Stock_Ticker.TYPE = SUBSTRING(Stock_Ticker.[TYPE], 1, 3)
    WHERE Stock_Ticker.unid = 123460;

