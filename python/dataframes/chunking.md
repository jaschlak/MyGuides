# Chunking

    Sometimes it is best to chunk through dataframes instead of iterating one at a time
    or mapping a huge column
    
## Build Example Dataframe

``` 
import pandas as pd
import numpy as np

# Create a sample large DataFrame
num_rows = 100000
data = {
    'Name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David'], num_rows),
    'Age': np.random.randint(20, 50, num_rows),
    'Score': np.random.randint(60, 100, num_rows),
    'Comments': np.random.choice(['Good job', 'Needs improvement', 'Excellent', 'Fair'], num_rows)
}

example_df = pd.DataFrame(data)
```


```

mychunksize = 5

def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


    
for myset in chunker(example_df,mychunksize):
    print(myset.shape)
    print(myset.iloc[0].keys())
    #print(myset)
```
