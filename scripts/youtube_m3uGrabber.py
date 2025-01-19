import requests
import os
import time 
from time import gmtime, strftime
from bs4 import BeautifulSoup

#change this to the URL you want to monitor
URL_TO_MONITOR = "https://www.youtube.com/c/24OnLive/live" 
response = requests.get(URL_TO_MONITOR)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Print the entire HTML source code
    #print(soup.encode("utf-8"))
    print(soup.prettify("UTF-8"))
    
    #for link in soup.find_all('a', href=True):
        #print(link['href'])
    
else:
    print(f"Error: {response.status_code}")
