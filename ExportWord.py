import pandas as pd
import os
from openpyxl import load_workbook

# Set the directory where your Excel files are located
folder_path = "your_folder_path_here"

# Store all combined data
all_data = []

# Loop through each Excel file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".xlsx"):
        file_path = os.path.join(folder_path, filename)
        xls = pd.ExcelFile(file_path)

        # Loop through each sheet that contains 'FSLA'
        for sheet_name in xls.sheet_names:
            if "FSLA" in sheet_name.upper():  # case-insensitive match
                df = pd.read_excel(xls, sheet_name=sheet_name, header=None)

                # Skip empty or invalid sheets
                if df.shape[1] < 2:
                    continue

                record = {
                    "File": filename,
                    "Sheet": sheet_name
                }

                for i in range(len(df)):
                    key = df.iat[i, 0]
                    value = df.iat[i, 1]
                    if pd.notna(key):  # Skip if key is NaN
                        record[str(key)] = value

                all_data.append(record)

# Combine all into one DataFrame
combined_df = pd.DataFrame(all_data)

# Save to Excel
combined_df.to_excel("combined_FSLA_output.xlsx", index=False)
