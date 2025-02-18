import requests
import zipfile
import io
import pandas as pd
import pycountry

# Step 1: Download the GeoNames cities file (cities with population >500)
url = 'http://download.geonames.org/export/dump/cities500.zip'
print("Downloading cities500.zip...")
response = requests.get(url)
if response.status_code == 200:
    # Extract the zip file in memory and then to a folder
    with zipfile.ZipFile(io.BytesIO(response.content)) as z:
        z.extractall('geonames_data')
    print("Download and extraction complete.")
else:
    print("Failed to download data")
    exit(1)

# Step 2: Read the extracted file into a DataFrame
# The file 'cities500.txt' contains tab-separated values.
filename = 'geonames_data/cities500.txt'

# GeoNames documentation (columns order):
# geonameid, name, asciiname, alternatenames, latitude, longitude, feature_class,
# feature_code, country_code, cc2, admin1 code, admin2 code, admin3 code, admin4 code,
# population, elevation, dem, timezone, modification date
columns = ['geonameid', 'name', 'asciiname', 'alternatenames', 'latitude', 'longitude',
           'feature_class', 'feature_code', 'country_code', 'cc2', 'admin1_code',
           'admin2_code', 'admin3_code', 'admin4_code', 'population', 'elevation',
           'dem', 'timezone', 'modification_date']

df = pd.read_csv(filename, sep='\t', header=None, names=columns, low_memory=False)

# Step 3: Map country codes to country names using pycountry
country_mapping = {country.alpha_2: country.name for country in pycountry.countries}
df['Country'] = df['country_code'].map(country_mapping)

# Step 4: Create a new DataFrame with only the Country and City (name) columns
result_df = df[['Country', 'name']].rename(columns={'name': 'City'})

# Optional: If you need a list of cities for a specific country (e.g., India), uncomment the following:
# result_df = result_df[result_df['Country'] == 'India']

# Step 5: Export the result to an Excel file
output_filename = 'countries_and_cities.xlsx'
result_df.to_excel(output_filename, index=False)
print(f"Excel file '{output_filename}' created successfully!")
