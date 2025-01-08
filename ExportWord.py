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
    word = row["Word"] if "Word" in row and pd.notna(row["Word"]) else None
    countries = str(row["Country"]).split(";") if pd.notna(row["Country"]) else []
    cities = str(row["City"]).split(";") if pd.notna(row["City"]) else []
    
    # Group cities by identical country occurrences
    unique_country_map = {}
    for country, city in zip(countries, cities):
        country = country.strip()
        city = city.strip()
        if country not in unique_country_map:
            unique_country_map[country] = {"countries": [], "cities": []}
        unique_country_map[country]["countries"].append(country)
        unique_country_map[country]["cities"].append(city)
    
    # Create rows for each unique country
    for country, data in unique_country_map.items():
        result_rows.append({
            "ID": id_,
            "Country": "; ".join(data["countries"]),
            "City": "; ".join(data["cities"]),
            "Word": word,
        })

# Convert processed rows to a DataFrame
output_df = pd.DataFrame(result_rows)

# Save the results to a new Excel file
output_df.to_excel(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")
