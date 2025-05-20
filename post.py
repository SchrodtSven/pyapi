import requests
import json

dta = {
    "id": 4,
    "name": "Atari BookST Pro 16/32",
    "data": {
        "year": 1988,
        "price": 3849.99,
        "CPU model": "68045",
        "Hard disk size": "80 MB",
    },
}

payload = json.dumps(dta)

# print (jd)


headers = {"content-type": "application/json"}
# payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
requestUrl = "https://api.restful-api.dev/objects/"
r = requests.put(requestUrl, data=payload, headers=headers)

print(r.content)

print(r.text)
