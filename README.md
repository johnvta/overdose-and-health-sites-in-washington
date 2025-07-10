# 🚑🗺️ Washington State Overdose & Health Services Finder 

A full-stack GIS web application designed to support public health and community infrastructure planning by mapping overdose events and available health services across Washington State.

![MIT License](https://img.shields.io/badge/License-MIT-green.svg)
![CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-blue.svg)
![Flask](https://img.shields.io/badge/Backend-Flask-lightgrey)
![Leaflet.js](https://img.shields.io/badge/Made%20With-Leaflet.js-brightgreen.svg)
![PostgreSQL](https://img.shields.io/badge/Database-PostgreSQL%20%2B%20PostGIS-blue)
![Render](https://img.shields.io/badge/Hosted%20on-Render-purple)

[🟢 Live Demo](https://washington-state-overdose-and-health.onrender.com/) • [📁 GitHub Repo](https://github.com/johnvta/wa-overdose-finder)


---

## 📍 Overview
This project visualizes the spatial relationship between overdose incidents and nearby health resources such as hospitals, emergency medical services, opioid treatment programs, non-opioid rehab facility, and harm reduction services. Built with a Flask backend and a Leaflet.js frontend, it allows users to interactively explore service coverage gaps and risk zones.

---

## 💡 Why It Matters

Washington’s overdose crisis varies sharply by location and by access to treatment. This map lets public health staff and policymakers:

- Spot counties with rising non‑fatal overdoses before deaths spike.
- Compare service coverage—hospitals, EMS, opioid‑treatment programs (OTP), non‑opioid rehab, harm‑reduction sites—against need.
- Prioritize funding or outreach where the gap is greatest.

---

## 🧭 Quick Tour

| Feature                               | Description                                                                | Preview       |
|---------------------------------------|----------------------------------------------------------------------------|---------------|
| **Choropleth toggle**                 | Switch between fatal and non-fatal overdose maps across two time periods   | *Coming soon* |
| **Healthcare icons + highlight ring** | View key services (EMS, OTP, rehab, harm reduction) with styled symbology  | *Coming soon* |
| **Search bar + address geocoding**    | Locate areas by address or ZIP code with instant map zoom                  | *Coming soon* |
| **Interactive legend + filters**      | Filter by overdose type, time, or service type                             | *Coming soon* |
| **Pop-ups with detail cards**         | Click map features to see site name, type, and relevant health details     | *Coming soon* |

---

## 🛠 Tech Stack

- **Frontend:** HTML, CSS, JavaScript, Leaflet.js  
- **Backend:** Flask (Python), RESTful API  
- **Database:** PostgreSQL + PostGIS  
- **Hosting/DevOps:** Supabase (DB), Render (API), GitHub Pages (frontend)

---

## ⚙️ Local Setup (Windows, Mac, Linux)

Set up the app locally using Python, PostgreSQL/PostGIS, and Flask.

> **Recommended for Windows:** Use **Git Bash** (comes with Git for Windows)  
> You can also use **Command Prompt** or **PowerShell** — see syntax notes below.  
> **Mac/Linux users:** Use your default terminal (e.g. Terminal).

---

### Set Up Python Virtual Environment

```bash
# 1. Clone the repository
git clone https://github.com/johnvta/wa-overdose-finder.git
cd wa-overdose-finder

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
## Git Bash (Windows)
source venv/Scripts/activate

## Command Prompt (Windows)
# venv\Scripts\activate

## Mac/Linux
# source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Create your local .env file
cp .env.example .env

# 6. Open the .env file in a text editor and update these values:
#    DB_HOST=your-db-host
#    DB_PORT=5432
#    DB_NAME=your-database-name
#    DB_USER=your-db-username
#    DB_PASSWORD=your-db-password

# 7. Run the Flask app
flask run

# 8. Open your browser and go to:
# http://127.0.0.1:5000
```
---

## 🔑 Environment Variables Reference

The app requires a `.env` file at the root directory to configure your database connection.

To start, copy the provided template:

```bash
cp .env.example .env
```

Then open `.env` in a text editor and replace the placeholder values with your actual PostgreSQL credentials.

```
DB_HOST=your-db-host
DB_PORT=5432
DB_NAME=your-database-name
DB_USER=your-db-username
DB_PASSWORD=your-db-password
```

| Variable       | Description                            | Example                |
|----------------|----------------------------------------|------------------------|
| `DB_HOST`      | Hostname of your PostgreSQL server     | `localhost`            |
| `DB_PORT`      | Port number for PostgreSQL             | `5432`                 |
| `DB_NAME`      | Name of your database                  | `wa_overdose_db`       |
| `DB_USER`      | PostgreSQL username                    | `postgres`             |
| `DB_PASSWORD`  | PostgreSQL password                    | `your_secure_password` |

> **Security Tip:** The `.env` file is excluded in `.gitignore` — do not commit it to version control.

---

## 📊 Data Sources

This application uses publicly available datasets related to overdose incidents and healthcare infrastructure in Washington State.

| Layer                                                              | Source                                    | Date Pulled | License       | Metadata                                                   |
|--------------------------------------------------------------------|-------------------------------------------|-------------|---------------|------------------------------------------------------------|
| County-level overdose counts (fatal & non-fatal)                   | WA Dept. of Health — Vital Statistics     | 2024‑03‑15  | Public Domain | [`county_overdose.xml`](docs/metadata/county_overdose.xml) |
| Healthcare sites (OTP, hospitals, EMS, rehab, harm reduction)      | SAMHSA OTP dataset + WA Health Facilities | 2025‑05‑10  | CC BY 4.0     | [`health_sites.xml`](docs/metadata/health_sites.xml)       |

> Full FGDC/ISO-19115 metadata files are included in [`docs/metadata/`](docs/metadata/)

---

## 🔌 API Endpoints

The Flask backend exposes two main REST endpoints that return spatial data as GeoJSON. These can be used by any frontend or client that supports GeoJSON.

| Method | Endpoint           | Description                                                                     | Returns                        |
|--------|--------------------|---------------------------------------------------------------------------------|--------------------------------|
| GET    | `/health_sites`    | Returns all healthcare locations (e.g. hospitals, OTP, harm reduction)          | `GeoJSON FeatureCollection`    |
| GET    | `/county_overdose` | Returns county polygons with fatal and non-fatal overdose statistics by year    | `GeoJSON FeatureCollection`    |

> 📎 These endpoints power the Leaflet.js frontend map and can be reused in other GIS tools or viewers that accept GeoJSON.

---

### Example Response (abbreviated)

**GET** `/health_sites`

```json
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "Point",
        "coordinates": [-122.33, 47.61]
      },
      "properties": {
        "name": "Harborview Medical Center",
        "type": "Hospital"
      }
    }
    // ...
  ]
}
```

---

## 📂 Project Structure

Below is the file structure for the `wa-overdose-finder` repository:

```
wa-overdose-finder/
├── app.py                      # Flask app (API + frontend)
├── requirements.txt            # Python dependencies
├── .env.example                # Template for environment variables
├── .gitignore                  # Files/folders excluded from Git
├── DATA_LICENSE.md             # License for data and icons
├── LICENSE.txt                 # MIT license for source code
├── README.md                   # Project documentation
├── converters/                 # Utility scripts
│   ├── address-to-coords.py        # Geocode addresses to coordinates
│   └── mercator-to-wgs84.py        # Coordinate projection converter
├── data/                       # Source data files
│   ├── fatal-overdose-wa-2003.geojson
│   ├── fatal-overdose-wa-2013.geojson
│   ├── nonfatal-overdose-wa-2003.geojson
│   ├── nonfatal-overdose-wa-2013.geojson
│   ├── health-sites-wa.csv
│   └── health-sites-wa.geojson
├── static/                     # Frontend assets served by Flask
│   ├── index.html
│   ├── main.js
│   ├── style.css
│   └── icons/                  # Custom map icons
│       ├── hospital.png
│       ├── ambulance.png
│       ├── opioid.png
│       ├── nonopioid.png
│       └── harmreduction.png
```
>  Each folder serves a specific purpose—keep it modular and documented for easier maintenance and collaboration.

---

## 🗺️ Roadmap

Planned improvements and future features for the Washington State Overdose & Health Services Finder:

- [ ] Add D3.js charts for overdose trends in popups
- [ ] Add location-based filters (e.g. “near me” radius search)
- [ ] Set up automated testing with `pytest` and GitHub Actions
- [ ] Add Docker support for easier local setup
- [ ] Add rate-limiting and input validation to API endpoints
- [ ] Publish OpenAPI (Swagger) spec for public API
- [ ] Automate data refreshes (annual overdose updates)

> Suggestions and contributions are welcome — feel free to open an issue or pull request!

---

## 📄 License

This project uses two licenses:

| Component        | License                                                                          | File                  |
|------------------|----------------------------------------------------------------------------------|-----------------------|
| **Source Code**  | [MIT License](https://opensource.org/licenses/MIT) — open for reuse              | `LICENSE.txt`         |
| **Data & Icons** | [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — attribution required | `DATA_LICENSE.md`     |

> 📌 You’re free to use, modify, and distribute this project. Please attribute appropriately and respect the license terms for datasets and visual assets.

## 📬 Contact

Created and maintained by [John Ta](mailto:johnvta.dev@gmail.com)  
📍 Seattle, WA  
📫 Email: [johnvta.dev@gmail.com](mailto:johnvta.dev@gmail.com)  
🔗 GitHub: [@johnvta](https://github.com/johnvta)

> Feel free to reach out for questions, feedback, or collaboration opportunities!