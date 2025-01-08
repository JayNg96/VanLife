import pandas as pd
import re

# File path
file_path = "your_file.xlsx"  # Replace with your file path

# Read the Excel file into a DataFrame
df = pd.read_excel(file_path)

# Extract the first column
column_data = df.iloc[:, 0].dropna()  # Drop any NaN values

# Lists to store names and ids
names = []
ids = []

# Regular expression to match ID pattern (letter followed by 6 digits, optionally enclosed in parentheses)
id_pattern = r'([a-zA-Z]{1}\d{6})'

# Iterate over each row in the column
for row in column_data:
    # Split by semicolon to get individual name-id pairs
    pairs = row.split(';')
    
    # Temporary lists for the current row
    row_names = []
    row_ids = []
    
    # Process each pair of name and ID
    for pair in pairs:
        # Find the ID using the regular expression
        match = re.search(id_pattern, pair)
        
        if match:
            # Extract the ID from the matched group
            row_ids.append(match.group(0))
            
            # Extract the name (everything before the ID or parentheses)
            name = re.sub(id_pattern, '', pair).strip()
            row_names.append(name)
        else:
            # If no ID is found, add the name and store NA for the ID
            name = pair.strip()
            row_names.append(name)
            row_ids.append('NA')
    
    # If there were no IDs found for any names, store 'NA' for each name
    if not any(id != 'NA' for id in row_ids):
        row_ids = ['NA'] * len(row_names)
    
    # Add the names and IDs for the current row to the main lists
    names.append(";".join(row_names))
    ids.append(";".join(row_ids))

# Create a new DataFrame with the names and ids
output_df = pd.DataFrame({
    'Names': names,
    'IDs': ids
})

# Save to a new Excel file
output_file_path = "output.xlsx"  # Replace with your desired output file path
output_df.to_excel(output_file_path, index=False)

print(f"Names and IDs have been extracted and saved to {output_file_path}")
