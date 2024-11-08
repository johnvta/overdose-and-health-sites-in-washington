import requests
import csv

# Set up OpenCage API
api_key = "3200904421b8466c97bb1ca2474a6db0"
api_url = "https://api.opencagedata.com/geocode/v1/json"

# Define input and output CSV file paths
input_file = "C:/Users/John/Desktop/portfolio/harm_reduction_sites.csv"
output_file = "C:/Users/John/Desktop/portfolio/harm_reduction_sites_wa.csv"

# Open both the input CSV file to read addresses and the output CSV file to save results
with open(input_file, newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    # Extend the original fieldnames to include new fields for city, latitude, and longitude
    fieldnames = reader.fieldnames + ["city", "latitude", "longitude"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Loop through each row in the input CSV
    for row in reader:
        # Construct the address to geocode by combining the 'Address' and 'State' fields
        address = f"{row['Address']}, {row['State']}"
        response = requests.get(api_url, params={"q": address, "key": api_key})
        # Check if the API response is successful
        if response.status_code == 200:
            data = response.json()
            # If there are results, extract latitude, longitude, and city (if available)
            if data['results']:
                # Get latitude and longitude
                row["latitude"] = data['results'][0]['geometry']['lat']
                row["longitude"] = data['results'][0]['geometry']['lng']
                
                # Get city if available
                components = data['results'][0]['components']
                row["city"] = components.get('city') or components.get('town') or components.get('village')
            else:
                row["latitude"], row["longitude"], row["city"] = None, None, None
        else:
            row["latitude"], row["longitude"], row["city"] = None, None, None
            
        # Write the updated row to the output CSV    
        writer.writerow(row)

