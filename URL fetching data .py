# main project 
# 1. get the web page - set a URL line of code to show what web page you are going to be extracting the data and information from. 
# 2. extracvt the data - as you will be writing the code of the specific URL WEB PAGE, you will then need to wite an extra script for exracting data and infromation for the database
# 3. transfer data and infromation from a web page to a WEB DB which stands for 'web database', you will need to transfer the webs infromation / data to a databse to keep it secured and accsesable for the devlper 

import requests
import re

def fetch_url(url):
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully fetched the URL.")
            html_content = response.text  # Fix: Changed 'response.tect' to 'response.text'
            return html_content
        else:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return None

# URL to fetch
url = "https://www.upliftedlingerie.co.uk"
html_content = fetch_url(url)

if html_content:
    # Do something with the HTML content if needed
    print("HTML content fetched successfully.")
   # print(html_content)
else:
    print("Unable to fetch HTML content.")

# Sample HTML content
html_content = """
<div class="div_menuitem">
    <a href="http://example.com/page1">Link 1</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page2">Link 2</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page3">Link 3</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page4">Link 4</a>
</div>
"""
 #print data into the database system for the website page 
# print data into the web database system for the URL fetching IN the PYTHON AND SQL code that has been scripted nto the second file project in URL data web scraping in SQL and python
# Regular expression to find URLs in div containers with class "div_menuitem"
url_pattern = re.compile(r'<div class="div_menuitem">.*?<a href="(http://[^"]+)"')

# Find all matching URLs
urls = url_pattern.findall(html_content)

# Take the first 3 URLs
urls = urls[:3]

# List to store the results
results = []

for url in urls:
    try:
        # Make a GET request to the URL
        response = requests.get(url)

        # Check if the response status code is 200
        if response.status_code == 200:
            results.append((url, "200 OK"))
        else:
            results.append((url, f"Error: {response.status_code}"))
    except requests.exceptions.RequestException as e:
        results.append((url, f"Exception: {e}"))

# Print the results
for url, status in results:
    print(f"URL: {url}, Status: {status}")

# below is a revised new code, including thease fixes that needed to be solved wihin the python code 
import requests 
import re 

def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("Successfully fetched the URL.")
            return response.text  # Fix: Changed 'response.tect' to 'response.text'
        else:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:  # Fix: Properly indented and spelled 'RequestException' correctly
        print(f"An error occurred: {e}")
        return None
import requests 
import re 

def fetch_url(url):
    try:
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            print("Successfully fetched the URL.")
            html_content = response.text
            return html_content
        else:
            print(f"Failed to fetch the URL. Status code: {response.status_code}")
            return None
        
    except requests.exceptions.requestsexeception as e:
        print(f"an error occurred: {e}")
        return None 
    
    # URL to fetch 
    url = "https://www.upliftedlingerie.co.uk"
    html_content = fetch_url(url)

    if html_content:
       # Do something with the HTML content if needed
     print("HTML content fetched successfully.")
    # Print a snippet instead of the entire content to avoid overload
    print(f"Snippet of HTML content: {html_content[:500]}")
    
    print("Unable to fetch HTML content.")

# Sample HTML content for regex example
html_content = """
<div class="div_menuitem">
    <a href="http://example.com/page1">Link 1</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page2">Link 2</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page3">Link 3</a>
</div>
<div class="div_menuitem">
    <a href="http://example.com/page4">Link 4</a>
</div>
"""
# regular expression to find the URLS in div containers with class "div_menuitem"
url_pattern=re.compile(r'<div class="div_menuitem">.*?<a href="(http://[^"]+)"')

# find all matching URLs 
urls = urls[:3]

# list to store the resluts 
resluts = []

for url in urls:
     try:
        #make a GET request to the url 
        response = requests.get(url)

        # check if the response status code is 200
        if response.status_code == 200:
            results.append((url, "200 OK"))
        else:
            resluts.append((url, f"error: {response.status_code}"))
     except requests.exceptions.RequestException as e: # i solved this errors due to some issues of how the code was scructures ##
        results.APPEND((URL, F"EXCEPTION: {e}"))

        # print the reluts 
        for url, status in resluts:
            print(f"URL: {url}, status: {status}")



        # regular expression to find URLs in div containers with class "div_menuitem"
url_pattern.findall(html_content)

        #tale the first 3 urls from the links tha have been provided on line 48 to 58
   
import csv 
import random 

# function to generate random data / infomaton 
def generate_random_data(num_records,num_fields):
    data = []
    for _ in range(num_records):
        record = [random.randint(1, 100) for _ in range(num_fields)]
        data.append(record)
        return data
    # function to save data to a csv file 
def save_to_csv(data, file, name): # this line of code would have a error due to the scucture of the code and how ist wriiten in such a form of way the code wa written 
     with open(filename, 'w', newline='')
as file:
       writer = csv.writter(file)
writer.writerows(data)

# main script 
if __name__ == "__main__":
    num_records = 100 # number of records 
    num_fields = 5 #number of fields per second 
    fieldname = 'random_data.csv'

    data = generate_random_data(num_records, num_fields=)
    
