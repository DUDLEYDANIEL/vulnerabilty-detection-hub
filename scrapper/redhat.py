import requests

def fetch_cve_data():
    # Define the API endpoint URL
    url = "https://access.redhat.com/hydra/rest/securitydata/cve.json"

    # Define query parameters to filter CVEs by date
    params = {
        "after": "2023-01-01",  # Example: Get CVEs reported after January 1, 2023
        "before": "2024-01-01"
    }

    # Make the GET request to the API
    response = requests.get(url, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the response JSON data
        data = response.json()

        # Print the data in CVE format
        for cve in data:
            print(f"CVE ID: {cve.get('CVE')}")
            print(f"Title: {cve.get('bugzilla_description')}")
            print(f"Severity: {cve.get('severity')}")
            print(f"Published Date: {cve.get('public_date')}")
            print(f"Description: {cve.get('details')[0] if 'details' in cve and cve['details'] else 'N/A'}")
            print(f"CVSS Score: {cve.get('cvss3_score', 'N/A')}")
            print(f"References: {cve.get('resource_url')}")
            print("-" * 50)
    else:
        print(f"Error: {response.status_code}")

fetch_cve_data()