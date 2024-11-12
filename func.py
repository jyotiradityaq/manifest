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
            print(f"Created Main Folder: {MAIN_FOLDER}")
        else:
            print(f"Main Foler Already Exists: {MAIN_FOLDER}")
        
    def connection(self, site):
        """Checks If The Website Is Reachable."""
        try:
            response = requests.get(site)
            return response.status_code == 200
        except requests.RequestException as e:
            print(f"Connection Error: {e}")
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
        """Gets The Source Code of The Given Website"""
        response = requests.get(site)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")
            self.mainFolder()
            try:
                with open(os.path.join(MAIN_FOLDER, "Source_Code.txt"), "w") as file:
                        file.write(soup.prettify())
                        print("+ Source Code Written To 'Source_Code.txt' In The Main Folder +")
            except IOError as e:
                print(f"Error Writing To File: {e}")
        else:
            print("+ Unable To Fetch Source Code. Website Is Not Reachable +")

    def getLinks(self, site):
        """Gets All The Links From The Website"""
        links = []
        response = requests.get(site)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "lxml")
            self.mainFolder()
            try:
                for link in soup.find_all('a', href=True):
                    href = link['href']
                    links.append(href)

                with open(os.path.join(MAIN_FOLDER, "Links.txt"), "a") as file:
                    for allLink in links:
                        file.write(allLink + "\n")
                    print("+ Links Written To 'Links.txt' In The Main Folder +")
            except IOError as e:
                print(f"Error Writing To File: {e}")
        else:
            print("+ Unable To Fetch Source Code. Website Is Not Reachable +")
