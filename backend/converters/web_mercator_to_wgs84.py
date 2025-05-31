import pandas as pd
from pyproj import Transformer
import geojson

# Load CSV file
df = pd.read_csv("health_sites_wa.csv")  

# Initialize transformer from Web Mercator (EPSG:3857) to WGS84 (EPSG:4326)
transformer = Transformer.from_crs("EPSG:3857", "EPSG:4326", always_xy=True)

# Convert each row's coordinates
df["longitude"], df["latitude"] = transformer.transform(df["lon"].values, df["lat"].values)

# Save the transformed DataFrame as a new CSV
df.to_csv("transformed_health_sites_wa.csv", index=False)

# Define a function to convert rows to GeoJSON format
def row_to_geojson(row):
    return geojson.Feature(
        geometry=geojson.Point((row["longitude"], row["latitude"])),
        properties=row.drop(["longitude", "latitude"]).to_dict()
    )

# Create GeoJSON features from each row
features = [row_to_geojson(row) for _, row in df.iterrows()]
feature_collection = geojson.FeatureCollection(features)

# Save the GeoJSON to a file
with open("health_sites_wa.geojson", "w") as f:
    geojson.dump(feature_collection, f)

print("GeoJSON file created successfully")
