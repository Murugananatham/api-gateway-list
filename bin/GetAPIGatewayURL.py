import sys
import os
import csv
from splunk.clilib.bundle_paths import make_splunkhome_path

def getURL():
    with open(make_splunkhome_path(['etc', 'apps', 'api-gateway-list',"lookups","api_gateway_urls_list.csv"]), newline='') as csvfile:
        csvData = csv.DictReader(csvfile)
        csvDataFormatted = {}
        for row in csvData:
            csvDataFormatted.update({row["Key"]:row["Value"]})
    print(csvDataFormatted)
getURL()