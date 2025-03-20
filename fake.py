import json
from faker import Faker
import random

fake = Faker()

# Bangalore coordinates range
BANGALORE_LAT = (12.85, 13.20)
BANGALORE_LON = (77.45, 77.75)
bu=369
# Common specialties (expand as needed)
SPECIALTIES  = [
    "Cardiology", 
    "Orthopedics", 
    "General Surgery", 
    "Pediatrics", 
    "Emergency Medicine", 
    "Obstetrics & Gynecology", 
    "Neurology", 
    "Dermatology", 
    "Gastroenterology", 
    "ENT (Otolaryngology)", 
    "Radiology", 
    "Anesthesiology", 
    "Internal Medicine", 
    "Pulmonology", 
    "Urology", 
    "Ophthalmology", 
    "Endocrinology", 
    "Nephrology", 
    "Psychiatry", 
    "Oncology"
]
SPECIALTY_IDS = list(range(1, 19))

def generate_hospital():
    lat = round(random.uniform(*BANGALORE_LAT), 4)
    lon = round(random.uniform(*BANGALORE_LON), 4)
    return {
        "model": "map.Hospital",  # Replace "your_app"
        "fields": {
            "name": fake.company() + " Hospital",
            "address": fake.street_address() + ", Bengaluru, Karnataka " + fake.postcode(),
            "district": bu, 
            "latitude": lat,
            "longitude": lon,
            "specialty": random.sample(SPECIALTY_IDS, k=random.randint(2, 3))
        }
    }

# Generate 200 hospitals
hospitals = [generate_hospital() for _ in range(40)]

# Save to JSON
with open("fake_hospitals.json", "w") as f:
    json.dump(hospitals, f, indent=2)

print("Fake data generated to fake_hospitals.json!")