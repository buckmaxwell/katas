import requests
import hashlib


resp = requests.get("https://api.close.com/buildwithus/")
key = resp.json()["key"]
traits = resp.json()["traits"]


post_body = []
for trait in traits:
    trait_hash = hashlib.blake2b(
        trait.encode(), digest_size=64, key=key.encode()
    ).hexdigest()
    post_body.append(trait_hash)

resp = requests.post("https://api.close.com/buildwithus/", json=post_body)
print(resp.text)  # Verification ID: 1741571151.YjEYjVPeou8
