import requests
import csv

# Set up OpenCage API
api_key = "3200904421b8466c97bb1ca2474a6db0"
api_url = "https://api.opencagedata.com/geocode/v1/json"

# Read addresses from CSV
input_file = "C:/Users/John/Desktop/portfolio/non_opioid_wa.csv"
output_file = "C:/Users/John/Desktop/portfolio/non_opioid_wa_coords.csv"

with open(input_file, newline='') as infile, open(output_file, mode='w', newline='') as outfile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames + ["latitude", "longitude"]
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        address = f"{row['Street']}, {row['City']}, {row['State']}"
        response = requests.get(api_url, params={"q": address, "key": api_key})
        if response.status_code == 200:
            data = response.json()
            if data['results']:
                row["latitude"] = data['results'][0]['geometry']['lat']
                row["longitude"] = data['results'][0]['geometry']['lng']
            else:
                row["latitude"], row["longitude"] = None, None
        writer.writerow(row)

