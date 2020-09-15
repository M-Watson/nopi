'''
nopi data functions
these functions operate with the data.nola.gov site for open data

'''

import requests


def get_catalog():
    catalog_url = "https://data.nola.gov/resource/7man-jc65.json"
    catalog = requests.get(catalog_url)
    return(catalog.json())
