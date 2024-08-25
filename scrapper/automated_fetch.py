#this is a automation file to automate to collect all the scarpping files 
import time
from redhat import fetch_cve_data

def run_automated():
    while True:
        fetch_cve_data()
        time.sleep(300)  # Sleep for 300 seconds (5 minutes)

if __name__ == '__main__':
    run_automated()  # Call the function to start the automated process
