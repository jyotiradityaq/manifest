# Libraries
import requests
from bs4 import BeautifulSoup
import os
import getpass

# Constants
MAIN_FOLDER = f"/home/{getpass.getuser()}/Desktop/_MANIFEST_"

class Website:
    def __init__(self, website):
        self.website = website
        
    def mainFolder(self):
        """Create The Main Folder If It Doesn't Exist"""
        if not os.path.exists(MAIN_FOLDER):
            os.mkdir(MAIN_FOLDER)
            print(f"Created main folder: {MAIN_FOLDER}")
        else:
            print(f"Main folder already exists: {MAIN_FOLDER}")
        
    def connection(self, site):
        """Checks If The Website Is Reachable."""
        try:
            response = requests.get(site)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Connection error: {e}")
            return False
                
    def testConnection(self, site):
        """Tests The Connection To The Given Website."""
        if self.connection(site):
            print("+ Connection Successfully Established +")
        else:
            print("+ Failed To Establish Connection +")
            print("+ Try Again Later +")
            exit()
    
    def sourceCode(self, site):
        pass