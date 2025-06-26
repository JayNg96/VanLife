import pandas as pd
import os

# Set the directory where your Excel files are located
folder_path = "your_folder_path_here"

# Store all combined data
all_data = []

# Loop through each Excel file
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        xls = pd.ExcelFile(file_path)

        for sheet_name in xls.sheet_names:
            if "FSLA" in sheet_name.upper():  # Only process sheets containing "FSLA"
                df = pd.read_excel(xls, sheet_name=sheet_name, header=None)

                if df.shape[1] < 2:  # Must have at least columns A and B
                    continue

                record = {
                    "File": filename,
                    "Sheet": sheet_name
                }

                for i in range(len(df)):
                    key = df.iat[i, 0]
                    if pd.isna(key):
                        continue

                    key_str = str(key)
                    # Use column C if 'abc' in key (case-insensitive)
                    if "ABC" in key_str.upper() and df.shape[1] >= 3:
                        value = df.iat[i, 2]
                    else:
                        value = df.iat[i, 1]

                    record[key_str] = value

                all_data.append(record)

# Combine and export
combined_df = pd.DataFrame(all_data)
combined_df.to_excel("combined_FSLA_output.xlsx", index=False)
