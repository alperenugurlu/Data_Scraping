# Data_Scraping
This was my first script written in 'python' language. Thank you for your attention.  It is a 'Data Scraping' script. It is a simple but useful script that can be used by anyone working in the field of Cyber ​​Security. All usage details are written in the readme file and source code. If you develop the program, I will be glad if you send it to me.

# Note:  

If you use it directly, the data that comes with the Script will provide you with xss payloads.


# How To ?

#Type in the address of the website you want to engrave data on.

#Click the right mouse button on the interface of the website to examine or check the item,
#find the titles related to the section you want to engrave ('div' - 'class') and write to this section. the example is as follows.

#example --> soup.find('details',{'class': 'xss-cheat-sheet-container-eventhandlers'})  

# How To Run ?

linux/ubuntu -->>  python3 data_scraping.py
windows -->> python data_scraping.py


# Libraries Required for the Program to Run:
#import request 
#from bs4 import beautifulsoup 

# writer: Alperen T. Ugurlu
# contact: https://www.linkedin.com/in/alperen-u-7b57b7178/
