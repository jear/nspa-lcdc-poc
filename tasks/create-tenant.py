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
    "authorization": "Bearer fa2e7317-93d6-448f-943c-6bed3ba53b71"
}

response = requests.post(url, json=payload, headers=headers, verify=False)

print(response.text)
