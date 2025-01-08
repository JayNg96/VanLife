import pandas as pd

# File paths
input_file = "input.xlsx"  # Replace with your input file path
output_file = "output.xlsx"  # Replace with your output file path

# Read the Excel file
df = pd.read_excel(input_file)

# Ensure the columns are named as expected
df = df.rename(columns={"id": "ID", "country": "Country", "city": "City"})

# Group the data by ID
result_rows = []

for id_, group in df.groupby("ID", dropna=False):  # Keep empty rows intact
    if pd.isna(id_):
        # Handle empty rows by appending them as-is
        result_rows.append({"ID": None, "Countries": None, "Cities": None})
        continue

    # Create lists to hold unique countries and corresponding cities
    country_city_map = {}
    for _, row in group.iterrows():
        country = row["Country"]
        city = row["City"]
        if pd.isna(country) or pd.isna(city):
            continue
        if country not in country_city_map:
            country_city_map[country] = []
        country_city_map[country].append(city)

    # Combine countries and cities for each unique ID
    for country, cities in country_city_map.items():
        result_rows.append({
            "ID": id_,
            "Countries": "; ".join([country] * len(cities)),
            "Cities": "; ".join(cities),
        })

# Convert results to a DataFrame
output_df = pd.DataFrame(result_rows)

# Save the results to a new Excel file
output_df.to_excel(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")
