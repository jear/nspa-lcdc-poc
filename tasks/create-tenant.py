import requests

url = "https://morpheus.lysdemolab.fr/api/accounts"

bearerToken=morpheus['morpheus']['apiAccessToken']
 
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer " + (bearerToken)
}
payload = { "account": {
        "role": { "id": 2 },
        "currency": "EUR",
        "name": "NR-Tenant",
        "subdomain": "NR-Subdomain",
        "description": "Tenant for NR"
    } }


response = requests.post(url, json=payload, headers=headers, verify=False)

print(response.text)
