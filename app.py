from flask import Flask, jsonify, send_from_directory, render_template, request
from flask_cors import CORS
import psycopg2, json, os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__, static_folder='static')
CORS(app, resources={r"/*": {"origins": [
    "http://127.0.0.1:5500",
    "https://washington-state-overdose-and-health.onrender.com"
]}})

# Database connection function
def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        sslmode='require'   
    )
    return conn

@app.route('/')
def serve_index():
    return send_from_directory(app.static_folder, 'index.html')

# Define a route to get health sites data
@app.route('/health_sites', methods=['GET'])
def health_sites():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # Select relevant data along with geometry as GeoJSON
    cur.execute("""
        SELECT amenity, name, address, city, state, zipcode, county, ST_AsGeoJSON(geom) 
        FROM health_sites;
    """)
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    # Format the data into a list of dictionaries
    features = []
    for row in rows:
        feature = {
            "type": "Feature",
            "geometry": json.loads(row[7]),
            "properties": {
                "amenity": row[0],
                "name": row[1],
                "address": row[2],
                "city": row[3],
                "state": row[4],
                "zipcode": row[5],
                "county": row[6]
            }
        }
        features.append(feature)


    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return jsonify(geojson)

# Define a route to get county overdose count
@app.route('/county_overdose', methods=['GET'])
def county_overdose():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("""
        SELECT 
            county, 
            population, 
            fatal_count_2003_07,
            fatal_capita_2003_07,
            fatal_count_2013_17,
            fatal_capita_2013_17,
            nonfatal_count_2003_07,
            nonfatal_capita_2003_07,
            nonfatal_count_2013_17,
            nonfatal_capita_2013_17,
            ST_AsGeoJSON(geom)
        FROM county_overdose;
    """)
    rows = cur.fetchall()
    
    cur.close()
    conn.close()
    
    features = []
    for row in rows:
        feature = {
            "type": "Feature",
            "geometry": json.loads(row[10]),
            "properties": {
                "county": row[0],
                "population": row[1],
                "fatal_count_2003_07": row[2],
                "fatal_capita_2003_07": row[3],
                "fatal_count_2013_17": row[4],
                "fatal_capita_2013_17": row[5],
                "nonfatal_count_2003_07": row[6],
                "nonfatal_capita_2003_07": row[7],
                "nonfatal_count_2013_17": row[8],
                "nonfatal_capita_2013_17": row[9]
            }
        }
        features.append(feature)

    geojson = {
        "type": "FeatureCollection",
        "features": features
    }
    
    return jsonify(geojson)

if __name__ == '__main__':
    app.run(debug=False)
