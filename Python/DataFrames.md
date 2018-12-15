# Pandas DataFrame Usage

    This is a workflow using DataFrames
    
## Dependencies

    import numpy as np                  # Needed for more advanced stuff
    import pandas as pd
    from numpy.random import randn
    
## Create and select data

    # Create dataframe
    np.random.seed(101)
    df = pd.DataFrame(randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])

    # Select a column from a DataFrame
    df['W']
    # or
    df.W

    # Select multiple columns (pass it a list of columns)
    df[['W','X','Y']]

    # Select multiple rows to report
    df.loc['A']

    # or

    df.iloc[0]


    # Select a single element using rows and columns together
    df.loc['B','Y']
    # or
    df.loc['B']['Y']


    # Select a subset of rows and columns
    df.loc[['A','B'],['X','Y']]
    
## Editing a DataFrame

    # Create a new column
    df['new'] = df['X'] + df['Y']

    # axis 0 = rows
    # axis 1 = columns

    # Drop a column
    df.drop('new', axis = 1, inplace = True)

    # Show number of rows and columns in DataFrame
    df.shape
    
## Selecting Subsets of information

    # Get conditional boolean values for a DataFrame
    booldf = df>.0

    # NaN values that are false from a DataFrame
    df[booldf]

    # or just
    df[df>0]

    # Get conditional boolean values for a row or column
    boolcol = df['W']>0

    # Return DataFrame with only columns that had non-null values
    df[boolcol]

    # or put it all together
    df[df['W']>0]


    #Only get a column from the results
    resultdf = df[df['W']>0]
    resultdf['X']

    # or simply
    df[df['W']>0]['X']


    # Return multiple conditions
    cond1 = df['W'] > 0
    cond2 = df['Y'] > 1

    df[(cond1) & (cond2)]
    df[(cond1) | (cond2)]
    
## Index  Information/Manipulation

    #Reset DataFrame numerical index
    df.reset_index(inplace = True)


    #Quick way to make a list for new indexing
    newind = 'CA NY WY OR CO'.split()
    df['States'] = newind

    # Make new column index
    df.set_index('States', inplace = True)

    # Select names of active index's
    df.index.names
    
## Multi-Level Indexing

    # Creating multi-level indexes
    outside = 'G1 G1 G1 G2 G2 G2'.split()
    inside = [1,2,3,1,2,3]
    # Combines the 2 lists into a list of tuple sets
    hier_index = list(zip(outside,inside))
    #Turns them into a multi-layer index, labels show the numerical instance of values
    hier_index = pd.MultiIndex.from_tuples(hier_index)

    # Selecting levels and labels
    hier_index.levels
    hier_index.labels

    # Creating a dataframe with multi-indexing
    df = pd.DataFrame(randn(6,2), hier_index,['A','B'])

    # Select subset from subIndex
    df.loc['G1']

    # Select sub-subset from multiindex
    df.loc['G1'].loc[1]

    # Select index names
    df.index.names # Gave no results

    # Give the multi indexes names
    df.index.names = ['Groups','Num']

    # Call single cell from 
    df.loc['G2'].loc[2]['B']


    # To get first values from each subIndex
    df.xs(1, level = 'Num')
