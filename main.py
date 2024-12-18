# Libraries

# Local Libraries
from func import Website

# Intro Screen

print("""
                                   /$$  /$$$$$$                      /$$    
                                  |__/ /$$__  $$                    | $$    
 /$$$$$$/$$$$   /$$$$$$  /$$$$$$$  /$$| $$  \__//$$$$$$   /$$$$$$$ /$$$$$$  
| $$_  $$_  $$ |____  $$| $$__  $$| $$| $$$$   /$$__  $$ /$$_____/|_  $$_/  
| $$ \ $$ \ $$  /$$$$$$$| $$  \ $$| $$| $$_/  | $$$$$$$$|  $$$$$$   | $$    
| $$ | $$ | $$ /$$__  $$| $$  | $$| $$| $$    | $$_____/ \____  $$  | $$ /$$
| $$ | $$ | $$|  $$$$$$$| $$  | $$| $$| $$    |  $$$$$$$ /$$$$$$$/  |  $$$$/
|__/ |__/ |__/ \_______/|__/  |__/|__/|__/     \_______/|_______/    \___/                                                                      
""")

print("""
===========================================================================
                        * Web Scrapper For Linux *
===========================================================================
""")

print("Enter Website: ")
usrSite = input("> ")

usrCls = Website(usrSite)
usrCls.mainFolder()

print("""
    1> Test Connection
    2> Create Main Folder/Check For Main Folder
    3> Get Source Code
    4> Get Links
""")

usrCommand = int(input("> "))

if usrCommand == 1:
    usrCls.testConnection(usrSite)
elif usrCommand == 2:
    usrCls.mainFolder()
elif usrCommand == 3:
    usrCls.sourceCode(usrSite)
elif usrCommand == 4:
    usrCls.getLinks(usrSite)