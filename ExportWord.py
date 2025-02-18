import geonamescache
import pandas as pd

# Initialize geonamescache
gc = geonamescache.GeonamesCache()

# Get countries and cities data
countries = gc.get_countries()
cities = gc.get_cities()

# Create a list of country-city pairs
country_city_list = []
for city_id, city_data in cities.items():
    country_code = city_data['countrycode']
    country_name = countries.get(country_code, {}).get('name', 'Unknown')
    city_name = city_data['name']
    country_city_list.append((country_name, city_name))

# Create a DataFrame and export to Excel
df = pd.DataFrame(country_city_list, columns=['Country', 'City'])
df.to_excel('countries_and_cities.xlsx', index=False)

print("Excel file created successfully!")
