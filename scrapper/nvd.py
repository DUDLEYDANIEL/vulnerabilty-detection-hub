import requests

# Define the API endpoint URL with the API key
url = "https://services.nvd.nist.gov/rest/json/cves/1.0/"

# Define the query parameters including the API key
params = {
    "apiKey": "//apikey will be here"  # Replace with your actual API key
}

try:
    # Make the GET request to the API with parameters
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Print the response text (JSON data)
        print(response.text)
    else:
        print(f"Error: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
