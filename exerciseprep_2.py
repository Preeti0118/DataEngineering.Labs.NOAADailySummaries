import urllib.request
import urllib.parse
import json
import os
from os import path
import pickle



headers = {'token': 'RtWMUMYImryAaCbuEqJBCqmfgtIfdeUw'}
myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=1'

request = urllib.request.Request(myurl, headers = headers)
file_path = './daily_summaries_FIPS10003_jan_2018_0.json'
with urllib.request.urlopen(request) as f:
    data = json.load(f)

    with open(file_path, 'w') as handler:
        json.dump(data, handler)



myurl = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/data?datasetid=GHCND&locationid=FIPS:10003&startdate=2018-01-01&enddate=2018-01-31&limit=1000&offset=1001'

request = urllib.request.Request(myurl, headers = headers)
file_path = './daily_summaries_FIPS10003_jan_2018_1.json'
with urllib.request.urlopen(request) as f:
    data = json.load(f)

    with open(file_path, 'w') as handler:
        json.dump(data, handler)
