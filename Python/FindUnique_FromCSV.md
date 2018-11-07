# Find unique values from a CSV

    Imports a csv and uses specified (path, file, and column inside csv)
    Finds duplicated values and lists them in order
    Works with both integers or strings

## Code:

    
    import pandas as pd
    path = "C://Users/jschlak/Desktop/TempLogs/MatsonAlarm/"
    file = 'caruthers-hs-users.csv'
    column = 5


    # Imports a csv and uses specified (path, file, and column inside csv)
    # Finds duplicated values and lists them in order
    # Works with integers or strings
    def unique_csv_duplicates(path,file,column):
        df = pd.read_csv(path+file)
        df=df.iloc[:,column]
        df = df[df.duplicated(keep=False)].drop_duplicates().sort_values().reset_index(drop=True)
        print(df[:])
        
        
    unique_csv_duplicates(path,file,column)
