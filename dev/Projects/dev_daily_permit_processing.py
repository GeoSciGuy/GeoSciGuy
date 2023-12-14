# Use date time to produce a text string with yesterdays date in it. 

import datetime
import os
import requests


yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
yesterday = yesterday.strftime('%Y%m%d')

print(yesterday)

# Path: dev/dev_daily_permit_processing.py

ndic_website = 'https://gis.dmr.nd.gov/downloads/oilgas/shapefile/'

example_filename = 'https://www.dmr.nd.gov/oilgas/daily/2023/dr060523.pdf'
dl_path = 'https://www.dmr.nd.gov/oilgas/daily/2023/'
file_name = 'dr' + yesterday + '.pdf'

dl_file = dl_path + file_name
file_path = '/Users/matthewherring/Documents/GitHub/GeoSciGuy/files'
print(dl_file)

# up one directory
os.chdir('..')
print(os.getcwd())
# change dirrectory to the file folder
os.chdir('files')
print(os.getcwd())