import requests

res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
type(res)

res.status_code == requests.codes.ok

len(res.text)

print(res.text[:250])

res.requests.get('http://:inventwithpython.com/page_that_does_not_exist')
res.raise_for_status()
# Always use the Raise after a Get to make sure that it works
# Use try and except to allow the program to keep moving 
# print(There was a problem : %s' % (exc)) # returns the error code, 404 in most cases


# The workflow is : 
# Call Requests.get() to download the file
# call open() with 'wb' to create a new file in write binary mode, preserves unicode
# Loop over the response object's iter_content() method
# call write() on each iteration to write the content to files
# call close() to close the file

# Beautiful Soup is suggested here to assist in working with webpages source code. 

# above example adapted to my NDIC daily permit PDF's
import requests

response = requests.get('https://www.dmr.nd.gov/oilgas/daily/2023/dr020123.pdf')
type(response)
response.status_code == requests.codes.ok
print(response.status_code == requests.codes.ok)
print(type(response))
print(response.text[:500])


# Import libraries
import requests
from bs4 import BeautifulSoup
  
# URL from which pdfs to be downloaded
# url = "https://www.geeksforgeeks.org/how-to-extract-pdf-tables-in-python/"
# url = 'https://www.dmr.nd.gov/oilgas/daily/2023/dr020123.pdf'
url = 'https://www.dmr.nd.gov/oilgas/dailyindex.asp'