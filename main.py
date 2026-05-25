import requests
from requests.auth import HTTPDigestAuth

url = "http://192.168.0.32/cgi-bin/snapshot.cgi?channel=1"

r = requests.get(
    url,
    auth=HTTPDigestAuth("admin", "admin@12345"),
    timeout=5
)

print("STATUS:", r.status_code)
print("CONTENT-TYPE:", r.headers.get("Content-Type"))


with open("snapshot.jpg", "wb") as f:
    f.write(r.content)