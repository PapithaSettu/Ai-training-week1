import csv
import json
import os

import requests
from dotenv import load_dotenv

BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(BASE, "..")          # project folder

#  API_KEY load 
load_dotenv(os.path.join(ROOT, "rest_api_task2", ".env"))
API_KEY = os.getenv("API_KEY")           


with open(os.path.join(ROOT, "employees.csv"), newline="") as f:
    rows = list(csv.DictReader(f))
for r in rows:
    r["salary"] = int(r["salary"])

high = [r for r in rows if r["salary"] > 50000]

with open(os.path.join(BASE, "employees.json"), "w") as f:
    json.dump(rows, f, indent=2)

with open(os.path.join(BASE, "high_earners.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(high)

print(f"Rows read: {len(rows)} | High earners: {len(high)}")

# API calls
URL = "https://jsonplaceholder.typicode.com/users"

headers = {"Authorization": f"Bearer {API_KEY}"}

try:
    resp = requests.get(URL, headers=headers, timeout=5)
    resp.raise_for_status()
    users = resp.json()

    for u in users[:1]:
        print(f"{u['id']} - {u['name']} - {u['email']}")

    # nested JSON 
    result = [
        {
            "id": u.get("id"),
            "name": u.get("name"),
            "city": u.get("address", {}).get("city"),
            "company": u.get("company", {}).get("name"),
        }
        for u in users
    ]
    with open(os.path.join(BASE, "users.json"), "w") as f:
        json.dump(result, f, indent=2)

    # 404 case
    missing = requests.get(f"{URL}/9999", headers=headers, timeout=5)
    if missing.status_code == 404:
        print("/users/9999 -> 404 Not found")

except requests.exceptions.Timeout:
    print("Error: request timed out")
except requests.exceptions.ConnectionError:
    print("Error: could not connect (internet / DNS check pannu)")
except requests.exceptions.HTTPError as err:
    print("HTTP error:", err)