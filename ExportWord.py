import pandas as pd

# File paths
input_file = "input.xlsx"  # Replace with your input file path
output_file = "output.xlsx"  # Replace with your output file path

# Read the Excel file
df = pd.read_excel(input_file)

# Prepare a list to hold processed rows
result_rows = []

# Iterate over each row in the input DataFrame
for _, row in df.iterrows():
    id_ = row["ID"]
    countries = str(row["Country"]).split(";") if pd.notna(row["Country"]) else []
    cities = str(row["City"]).split(";") if pd.notna(row["City"]) else []
    word = row["Word"] if "Word" in row and pd.notna(row["Word"]) else None
    
    # Check if there are multiple unique country-city pairs
    if len(set(countries)) > 1:  # If there are multiple unique countries
        seen = set()
        combined_country = []
        combined_city = []
        for country, city in zip(countries, cities):
            if (country, city) not in seen:
                combined_country.append(country.strip())
                combined_city.append(city.strip())
                seen.add((country, city))
        
        # Add combined country and city to the result
        result_rows.append({
            "ID": id_,
            "Country": "; ".join(combined_country),
            "City": "; ".join(combined_city),
            "Word": word,
        })
    else:
        # If all countries are the same, keep them combined in one row
        result_rows.append({
            "ID": id_,
            "Country": "; ".join(countries),
            "City": "; ".join(cities),
            "Word": word,
        })

# Convert processed rows to a DataFrame
output_df = pd.DataFrame(result_rows)

# Save the results to a new Excel file
output_df.to_excel(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")
