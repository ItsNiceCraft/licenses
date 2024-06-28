import requests
from os import path, mkdir

if not path.exists("licenses"):
    mkdir("licenses")

res = requests.get("https://api.github.com/licenses")
if res.status_code != 200:
    print("Error receiving licenses")
    exit(1)
for gh_license in res.json():
    res_license = requests.get(gh_license["url"])
    if res_license.status_code != 200:
        print(f"Error receiving license {gh_license['key']}")
        exit(1)
    with open(f"licenses/{gh_license['key']}.txt", "w") as f:
        f.write(res_license.json()["body"])
