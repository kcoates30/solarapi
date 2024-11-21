import requests

# API Key and Base URL
API_KEY = "AIzaSyDhz7Lcfbci1DjpQZyQyl57mACNYrpptCw"
BASE_URL = "https://solar.googleapis.com/v1/buildingInsights:findClosest?"

# Define Parameters (Example: Address-based analysis)
params = {
    "location.latitude": 37.4450,
    "location.longitude": -122.1390,
    "requiredQuality": "low",
    "key": API_KEY,
}

# Make the Request
response = requests.get(BASE_URL, params=params)

# Check the Response
if response.status_code == 200:
    data = response.json()
    print("Solar Data:", data)
else:
    print("Error:", response.status_code, response.text)
