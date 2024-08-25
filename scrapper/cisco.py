import requests

# ----------------------- Step 1: Obtain the Authorization Token ----------------------------#

# URL of the API endpoint for token retrieval
token_url = "https://id.cisco.com/oauth2/default/v1/token"

# Data to be sent in the POST request to obtain the token
token_data = {
    "client_id": "4e3uyfuh5q35na62v6rfr5w4",
    "client_secret": "Wa3cE5TBMnrMNu5fJWjQ58Aj",
    "grant_type": "client_credentials",
}

# Headers for the token request
token_headers = {"Content-Type": "application/x-www-form-urlencoded"}

# Making the POST request to get the token
token_response = requests.post(
    token_url, headers=token_headers, data=token_data, verify=False
)

# Checking if the token request was successful
if token_response.status_code == 200:
    # Extract the access token from the response
    token = token_response.json().get("access_token")
    print("Token obtained successfully!")
else:
    print(f"Failed to obtain token. Status code: {token_response.status_code}")
    print(token_response.text)
    exit()

# ----------------------- Step 2: Use the Token to Get Vulnerability Data ----------------------------#

# URL to get the latest vulnerabilities
vuln_url = "https://apix.cisco.com/security/advisories/v2/latest/10"

# Headers for the vulnerability data request, including the Authorization token
vuln_headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}

# Making the GET request to retrieve vulnerability data
vuln_response = requests.get(vuln_url, headers=vuln_headers, verify=False)

# Checking if the vulnerability request was successful
if vuln_response.status_code == 200:
    # Parsing the JSON response
    vulnerabilities = vuln_response.json()

    # counting purpose
    i = 1

    # Pretty print the JSON data
    advisories = vulnerabilities.get("advisories", [])
    for advisory in advisories:

        ProductNames = advisory.get("productNames", "N/A")
        Severity = advisory.get("severity", "N/A")
        Vulnerability = advisory.get("summary", "N/A").replace("\\r\\n\\p", " ").strip()
        Mitigation = advisory.get("publicationUrl", "N/A")
        PublicationDate = advisory.get("publicationDate", "N/A")
        Cves = advisory.get("cves", "N/A")

        # Formatting and data extration for obtained data
        print(f"{i} - Vulnerability\n")
        print(f"Product Name: {ProductNames}")
        print(f"Product Version: N/A")
        print("OEM Name: Cisco")
        print(f"Severtiy Level: {Severity}")
        print(f"Vulnerability: {Vulnerability}")
        print(f"Mitigation Strategy: {Mitigation}")
        print(f"Published Date: {PublicationDate}")
        print(f"Unique ID: {Cves}\n")
        print("END\n\n")
        i += 1
else:
    print(
        f"Failed to retrieve vulnerability data. Status code: {vuln_response.status_code}"
    )
    print(vuln_response.text)
