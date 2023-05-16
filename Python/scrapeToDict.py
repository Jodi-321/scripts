from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import os

#scipt scrapes keywords, and cleans pseudo-content to be added as keywords
url = "https://www.treasurydirect.gov/help-center/glossary-of-terms/"

#stores webpage in variable
content = requests.get(url)

#converts webpage data to text
content_text = content.text

#parses thorugh text looing for HTML tags
soup = BeautifulSoup(content_text, 'html.parser')

#stores specific HTML tags in variable
tbl = soup.find("dl", {"class":"dictionary-terms"})

#variable to search for strings that need additional cleaning before adding to dictionary
forbidden = re.compile('dt id')

# for loop runs through HTML document store in ***tbl**
for x in tbl:

    #checks each iteration for 'dt' tags
    for y in soup.find_all('dt'):

        #if variale needs additional cleaning this if statemnet checks
        if forbidden.search(str(y)):
            #regex to take all variables and only pull data between ">  <"
            test = re.findall('\>(.* ?)\<',str(y))

            #begin populating list with clean data. If lenth is less than 4, it is skipped
            for y in test:
                if len(y) < 4:
                    continue
                else:
                    print(y,sep="\n")

        # If no data needs to be cleaned, it gets added to final list
        else:
            #pull data between ">  <" tags
            test2 = re.findall('\>(.* ?)\<',str(y))

            #populate final list. If data is less than 4 charactes, it is skipped
            for y in test2:
                if len(y) < 4:
                    continue
                else:
                    print(y,sep="\n")
                    
                    