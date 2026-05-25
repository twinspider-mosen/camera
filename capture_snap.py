import requests
from requests.auth import HTTPDigestAuth
from datetime import datetime
import os

url = "http://192.168.0.32/cgi-bin/snapshot.cgi?channel=1"

r = requests.get(
    url,
    auth=HTTPDigestAuth("admin", "admin@12345"),
    timeout=5
)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("Content-Type"))

if r.status_code == 200:
    # create folder (optional but recommended)
    os.makedirs("snapshots", exist_ok=True)

    # timestamp filename (safe + sortable)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S_%f")

    file_path = f"snapshots/snapshot_{timestamp}.jpg"

    with open(file_path, "wb") as f:
        f.write(r.content)

    print("Saved:", file_path)
else:
    print("Failed to fetch snapshot")

    