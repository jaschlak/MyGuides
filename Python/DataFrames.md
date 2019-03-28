# Pandas DataFrame Usage

    This is a workflow using DataFrames
    
## Dependencies

    import numpy as np                  # Needed for more advanced stuff
    import pandas as pd
    from numpy.random import randn
    
## Create and select data

    ## Create dataframe
    
        np.random.seed(101)
        df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
        
    ## Create dataframe from lists
    
        df = pd.DataFrame.from_dict({'<list name>':<list variable>, '<list 2 name>':<list 2 variable>});

    ## Select a column from a DataFrame
    
        df['W']
    
    ## or
    
        df.W

    ## Select multiple columns (pass it a list of columns)
        df[['W','X','Y']]

    ## Select multiple rows to report
        
        df.loc['A']
        or
        df.iloc[0]


    ## Select a single element using rows and columns together
    
        df.loc['B','Y']
        or
        df.loc['B']['Y']


    ## Select a subset of rows and columns
        
        df.loc[['A','B'],['X','Y']]
    
# Editing a DataFrame

    ## Create a new column
    
        df['new'] = df['X'] + df['Y']

        note:
        axis 0 = rows
        axis 1 = columns

    ## Drop a column
    
        df.drop('new', axis = 1, inplace = True)

    ## Show number of rows and columns in DataFrame
    
        df.shape
    
# Selecting Subsets of information

    ## Get conditional boolean values for a DataFrame
    
        booldf = df>.0

    ## NaN values that are false from a DataFrame
    
        df[booldf]
        or just
        df[df>0]

    ## Get conditional boolean values for a row or column
        boolcol = df['W']>0

    ## Return DataFrame with only columns that had non-null values
    
        df[boolcol]
        or put it all together
        df[df['W']>0]

    ## Only get a column from the results
        
        resultdf = df[df['W']>0]
        resultdf['X']

    ## or simply
        
        df[df['W']>0]['X']


    ## Return multiple conditions
    
        cond1 = df['W'] > 0
        cond2 = df['Y'] > 1

        df[(cond1) & (cond2)]
        df[(cond1) | (cond2)]
    
# Dealing with Null values

    ## See if DataFrame contains null values
    
        df.isnull()

    ## Drops NaN rows/columns
    
        df.dropna()
        df.dropna(axis = 1)
    
    ## Require 2 amount of values to be null before dropping
    
        df.dropna(thresh = 2)
    
    ## Fill null value with something
    
        df.fillna(value = 'Something')
    
    ## Fill null values with mean of column
    
        df.fillna(value = df['A'].mean())
        or one liner
        df.groupby('Company').sum().loc['FB']
    
# Index  Information/Manipulation

    ## Report DataFrame without index
        df.to_string(index = False)

    ## Reset DataFrame numerical index (keep old)
        df.reset_index(inplace = True)

        ## Reset DataFrame numerical index (don't keep old)
        df.reindex()
        or 
        df.reset_index(drop = True,inplace = True)


    ## Quick way to make a list for new indexing
        
        newind = 'CA NY WY OR CO'.split()
        df['States'] = newind

    ## Make new column index
        
        df.set_index('States', inplace = True)

    ## Select names of active index's
        
        df.index.names
        or
        df.index                            # Gives more info
        
    ## Get names of columns
    
        df.columns
    
# Multi-Level Indexing

    ## Creating multi-level indexes

        outside = 'G1 G1 G1 G2 G2 G2'.split()
        inside = [1,2,3,1,2,3]
    
    ## Combines the 2 lists into a list of tuple sets
    
        hier_index = list(zip(outside,inside))
    
    ## Turns them into a multi-layer index, labels show the numerical instance of values
    
        hier_index = pd.MultiIndex.from_tuples(hier_index)

    ## Selecting levels and labels
    
        hier_index.levels
        hier_index.labels

    ## Creating a dataframe with multi-indexing
    
        df = pd.DataFrame(randn(6,2), hier_index,['A','B'])

    ## Select subset from subIndex
    
        df.loc['G1']

    ## Select sub-subset from multiindex
    
        df.loc['G1'].loc[1]

    ## Select index names
    
        df.index.names # Gave no results

    ## Give the multi indexes names
    
        df.index.names = ['Groups','Num']

    ## Call single cell from 
    
        df.loc['G2'].loc[2]['B']

    ## To get first values from each subIndex
    
        df.xs(1, level = 'Num')
    
# Grouping

    ## Setup data for testing
    
        data = {'Company':'GOOG GOOG MSFT MSFT FB FB'.split(), \
                   'Person':'Sam Charlie Amy Vanessa Carl Sarah'.split(), \
                   'Sales':[200,120,340,124,243,350]}

    ## Turn data into DataFrame
    
        df = pd.DataFrame(data)
    
    ## Group DataFrame by company
        
        byComp = df.groupby('Company')
    
    # Take in group, select aggrigate data 
    
        byComp.mean()
        byComp.sum()
        byComp.std()
        byComp.count()
        byComp.max()
        byComp.min()
        byComp.describe()                   # reports several aggrigates
        byComp.describe().transpose()
        
# Merging Joining Concatinating (Find examples from video/.zip)

    ## Concatinate
        
        pd.concat([df1,df2,df3])            #Concat on columns
        pd.concat([df1,df2,df3],axis = 1)   #Concat on rows
    
    ## Merge (keys must align)
    
        pd.merge(df1, df2, how = 'inner', on = 'key')
        pd.merge(df1, df2, on = ['key1, key2])
    
    ## Joining (like merge but keys are in index, not column)
        df1.join(df2, how = 'outer')
    
# Operations

    ## Find all unique values for DataFrame
        
        df['column2'].unique()
    
    ## Find number of values that are unique
    
        len(df['col2'].unique())
        or
        df['col2'].nunique()
        
    ## Table of unique values and how many timmes they show up
    
        df['col2'].value_counts()
        
    ## Apply a function to a selection of data
    
        cond1 = df['col1'] > 2
        cond2 = df['col2'] == 4
        
        def times2(x):
            return x*2
        
        df[(cond1) & (cond2)].apply(times2)     # Apply custom function
        or
        df[(cond1) & (cond2)].apply(lambda x: x*2)
        
        df[(cond1) & (cond2)].sum()             # Apply built in function
        or
        df[(cond1) & (cond2)].apply(len)
        
# Sorting and Ordering

    ## Sorting by column
    
        df.sort_values('col2')                      # Note indexes follow presorted order
    
    ## Pivot Table (Turns data with matching layers of indexes into Multi-layer indexes)
 
        # Setup DataFrame can be found in video or .zip (multiple indexes must align)
        df.pivot_table(values = 'colD', index = ['indexA', 'indexB'], columns = ['colC'])
    
# Data input/output (CSV, Excel, HTML, SQL)

    ## Dependencies that must be installed via pip ect.
    
        sqlalchemy                                  # SQL
        lxml                                        # XML
        html5lib                                    # html
        BeautifulSoup4
        
    ## See file location
    
        pwd
        
    ## Read CSV file to a DataFrame
    
        pd.read_csv('file_name.csv')
        
        note:
        pandas can read a lot of files using the pd.read_*** function
        
    ## Writing DataFrame to a csv
    
        df = pd.read_csv('filename.csv')
        or
        df.to_csv('my_output', index = False)           # Doesn't save index as a column, saves numerical index instead
        
    ## Read entire txt document as DataFrame

        df = pd.read_fwf(path, widths = [1000])                     # widths is a list of how long you want each column to be, this example makes a single column
     
    ## Import Excel Sheet to DataFrame
    
        note: cannot import formulas
        
        pd.read_excel('filename.xlsx', sheetname = 'sheet1')                  # 1 sheet at a times2
        
    ## Export DataFrame to Excel Sheet
    
        df.to_excel('filename.xlsx', sheet_name = 'sheet1')
        
    ## Import html to List of DataFrames
    
        data = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html')
        
    ## Extract DataFrame from imported html list
    
        df = data[0].head()

    ## SQLite Dependency
    
        from sqlalchemy import create_engine        #note: This is for SQLite, look up your driver
    
    ## Create Temperary SQL Engine
    
        engine = create_engine('sqlite:///:memory')
    
    ## Create DataFrame from temp SQL engine
    
        df.tosql('my_table', engine)
        
    ## Create DataFrame connection from SQL engine
    
        sqldf = pd.read_sql('my_table', con = engint)
        
        
    

