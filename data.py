import pandas as pd
import json

# Read the CSV file (ensure the path is correct)
df = pd.read_csv('extracted_data_unique.csv')

# Get unique states from the CSV
unique_states = df['statename'].unique()

fixture = []
state_pk_map = {}  # To map state names to primary keys
state_pk = 1
distict_pk = 1

# Create fixture entries for states
for state_name in unique_states:
    fixture.append({
        "model": "map.state",  # Replace "yourapp" with your actual app label
        "pk": state_pk,
        "fields": {
            "name": state_name
        }
    })
    state_pk_map[state_name] = state_pk
    state_pk += 1

# Create fixture entries for districts
for _, row in df.iterrows():
    state_name = row['statename']
    district_name = row['district']
    fixture.append({
        "model": "map.district",  
        "pk": distict_pk,
        "fields": {
            "name": district_name,
            "state": state_pk_map[state_name]
        }
    })
    distict_pk += 1

# Write the fixture to a JSON file
with open('fixture_states_disticts.json', 'w') as f:
    json.dump(fixture, f, indent=4)

print("Fixture generated successfully!")
