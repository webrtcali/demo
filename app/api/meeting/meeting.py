# pip3 install requests
# pip3 install requests
import requests
import json

API_KEY = "Rogachat_default_secret"
Rogachat_URL = "https://.Rogachat.com/api/v1/meeting"
# Rogachat_URL = "http://localhost:3010/api/v1/join"

headers = {
    "authorization": API_KEY,
    "Content-Type": "application/json",
}

response = requests.post(
    Rogachat_URL,
    headers=headers
)

print("Status code:", response.status_code)
data = json.loads(response.text)
print("meeting:", data["meeting"])
