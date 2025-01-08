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

for id_, group in df.groupby("ID"):
    countries = group["Country"].tolist()
    cities = group["City"].tolist()
    
    # Create a dictionary to ensure one country-city pair per row
    unique_pairs = {}
    for country, city in zip(countries, cities):
        if country not in unique_pairs:
            unique_pairs[country] = []
        unique_pairs[country].append(city)

    # Add the first country-city pair to the main row
    base_row = {"ID": id_, "Countries": "", "Cities": ""}
    remaining_rows = []

    for country, city_list in unique_pairs.items():
        if base_row["Countries"] == "":
            base_row["Countries"] = "; ".join([country] * len(city_list))
            base_row["Cities"] = "; ".join(city_list)
        else:
            # For additional country-city pairs, add them to separate rows
            remaining_rows.append(
                {"ID": id_, "Countries": "; ".join([country] * len(city_list)), "Cities": "; ".join(city_list)}
            )
    
    result_rows.append(base_row)
    result_rows.extend(remaining_rows)

# Convert results to a DataFrame
output_df = pd.DataFrame(result_rows)

# Save the results to a new Excel file
output_df.to_excel(output_file, index=False)

print(f"Data has been processed and saved to {output_file}")
