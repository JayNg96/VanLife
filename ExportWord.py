import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_cities_from_wikipedia(country):
    """
    Fetches the list of cities from the Wikipedia page for a given country.
    This example assumes the page is titled "List of cities in <country>".
    """
    page_title = f"List of cities in {country}"
    endpoint = "https://en.wikipedia.org/w/api.php"
    params = {
        "action": "parse",
        "page": page_title,
        "format": "json",
        "prop": "text",
        "redirects": True  # follow redirects if page title changes
    }
    
    response = requests.get(endpoint, params=params)
    data = response.json()
    
    # Check if the page was retrieved successfully
    if "error" in data:
        print(f"Error retrieving page for {country}: {data['error'].get('info', 'Unknown error')}")
        return []
    
    # Extract HTML content from the JSON response
    html_content = data["parse"]["text"]["*"]
    soup = BeautifulSoup(html_content, "html.parser")
    
    cities = []
    
    # Find all tables with the 'wikitable' class (common for such lists)
    tables = soup.find_all("table", {"class": "wikitable"})
    for table in tables:
        rows = table.find_all("tr")
        # Skip header row and extract the first cell (assumed to contain the city name)
        for row in rows[1:]:
            cells = row.find_all(["td", "th"])
            if cells:
                # Get the text of the first cell and remove any extra whitespace
                city = cells[0].get_text(strip=True)
                if city and city not in cities:  # avoid duplicates
                    cities.append(city)
    return cities

# Specify the country
country = "India"
cities = get_cities_from_wikipedia(country)

if cities:
    # Create a DataFrame with two columns: Country and City
    df = pd.DataFrame({"Country": [country] * len(cities), "City": cities})
    
    # Export to an Excel file
    output_filename = "wikipedia_cities.xlsx"
    df.to_excel(output_filename, index=False)
    print(f"Excel file '{output_filename}' created successfully with {len(cities)} cities from {country}!")
else:
    print("No cities found or an error occurred.")
