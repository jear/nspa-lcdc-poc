import requests

url = "https://morpheus.lysdemolab.fr/api/accounts"

payload = { "account": {
        "role": { "id": 2 },
        "currency": "EUR",
        "name": "NR-Tenant",
        "subdomain": "NR-Subdomain",
        "description": "Tenant for NR"
    } }
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + (bearerToken)
}

response = requests.post(url, json=payload, headers=headers, verify=False)

print(response.text)
