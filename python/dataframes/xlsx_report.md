# XLSX Report

    It is often handy to be able to push your dataframe to a report in xlsx form
    
## Example

```
import pandas as pd

output_filepath = output_path = 'output/report_name.xlsx'

# Sample DataFrame with extra whitespace
data = {
    'Name': [' Alice ', ' Bob ', ' Charlie ', ' David '],
    'Age': [24, 27, 22, 32],
    'Score': [85, 88, 90, 78],
    'Comments': [' Good job ', ' Needs improvement ', ' Excellent ', ' Fair ']
}
df = pd.DataFrame(data)
```

```
# Function to calculate column width
def get_optimal_column_width(series, header, padding=2):
    # Calculate the maximum length of the column contents and header
    max_len = max(series.astype(str).map(len).max(), len(header))
    if max_len > 90:
        max_len = 90
        
    return max_len + padding  # Add padding for readability
```

```
def df_to_xlsx(df):
    
    # Strip whitespace from all string columns
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    
    # Export to Excel with xlsxwriter for additional formatting
    with pd.ExcelWriter('{}.xlsx'.format(output_filepath), engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Sheet1', index=False)
    
        # Access the xlsxwriter workbook and worksheet objects
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']
    
        # Add a header format
        header_format = workbook.add_format({
            'bold': True,
            'text_wrap': True,
            'valign': 'top',
            'fg_color': '#D7E4BC',
            'border': 1
        })
    
        # Write the column headers with the defined format
        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
    
        # Set the column width based on the largest entry in each column
        for i, col in enumerate(df.columns):
            optimal_width = get_optimal_column_width(df[col], col)
            worksheet.set_column(i, i, optimal_width)
    
    print("DataFrame exported successfully!")
```