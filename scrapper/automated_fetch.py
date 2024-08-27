#this is a automation file to automate to collect all the scarpping files 
import time
from redhat import fetch_cve_data
from cisco import get_cisco_vulnerabilities
# "client_id": "",
#client_secret": "",

def run_automated():
    while True:
        fetch_cve_data()
        print("Data fetched successfully! from Redhat")
        client_id = "4e3uyfuh5q35na62v6rfr5w4"
        client_secret = "Wa3cE5TBMnrMNu5fJWjQ58Aj"
        get_cisco_vulnerabilities(client_id, client_secret)
        time.sleep(300)  # Sleep for 300 seconds (5 minutes)

if __name__ == '__main__':
    run_automated()  # Call the function to start the automated process
