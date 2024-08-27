import requests

def get_cisco_vulnerabilities(client_id, client_secret):
    # Step 1: Obtain the Authorization Token
    token_url = "https://id.cisco.com/oauth2/default/v1/token"
    token_data = {
        "client_id": client_id,
        "client_secret": client_secret,
        "grant_type": "client_credentials",
    }
    token_headers = {"Content-Type": "application/x-www-form-urlencoded"}
    
    # Making the POST request to get the token
    token_response = requests.post(token_url, headers=token_headers, data=token_data, verify=False)
    
    # Checking if the token request was successful
    if token_response.status_code == 200:
        token = token_response.json().get("access_token")
        print("Token obtained successfully!")
    else:
        print(f"Failed to obtain token. Status code: {token_response.status_code}")
        print(token_response.text)
        return
    
    # Step 2: Use the Token to Get Vulnerability Data
    vuln_url = "https://apix.cisco.com/security/advisories/v2/severity/critical"
    vuln_headers = {"Accept": "application/json", "Authorization": f"Bearer {token}"}
    
    # Making the GET request to retrieve vulnerability data
    vuln_response = requests.get(vuln_url, headers=vuln_headers, verify=False)
    
    # Checking if the vulnerability request was successful
    if vuln_response.status_code == 200:
        vulnerabilities = vuln_response.json()
        advisories = vulnerabilities.get("advisories", [])
        
        # Process and print the vulnerability data
        for i, advisory in enumerate(advisories, start=1):
            product_names = advisory.get("productNames", "N/A")
            severity = advisory.get("severity")
            vulnerability = advisory.get("summary", "N/A").replace("\\r\\n\\p", " ").strip()
            mitigation = advisory.get("publicationUrl", "N/A")
            publication_date = advisory.get("publicationDate", "N/A")
            cves = advisory.get("cves", "N/A")
            
            # Formatting and data extraction for obtained data
            print(f"{i} - Vulnerability\n")
            print(f"Product Name: {product_names}")
            print(f"Product Version: N/A")
            print("OEM Name: Cisco")
            print(f"Severity Level: {severity}")
            print(f"Vulnerability: {vulnerability}")
            print(f"Mitigation Strategy: {mitigation}")
            print(f"Published Date: {publication_date}")
            print(f"Unique ID: {cves}\n")
            print("END\n\n")
    else:
        print(f"Failed to retrieve vulnerability data. Status code: {vuln_response.status_code}")
        print(vuln_response.text)

# Example usage in another file
if __name__ == "__main__":
    client_id = "4e3uyfuh5q35na62v6rfr5w4"
    client_secret = "Wa3cE5TBMnrMNu5fJWjQ58Aj"
    get_cisco_vulnerabilities(client_id, client_secret)
