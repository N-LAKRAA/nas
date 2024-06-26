#import csv 

# with open("valeurs_annuelles.csv") as csv_file:
#     reader = csv.reader(csv_file, delimiter=';')
#     data = list(reader)
    
#     for row in data:
#         row.pop()
#         print(row)
#     csv_file.close()
#age = 30
#isAdult = age > 17

#print(isAdult)

import json, requests, os, csv, math
import xmltodict
from requests.auth import HTTPBasicAuth
USERNAME = "pub"
API_KEY = "fYqyWKEa"
BUCKET = os.environ["HOME"] + "/dev/statitb3/insee/"
KEYS = f"{BUCKET}/principaux/keys.csv"
METAMAP = f"{BUCKET}/principaux/meta.json"
UNITSMAP = f"{BUCKET}/units.json"
FREQUENCIESMAP = f"{BUCKET}/frequencies.json"

URL_SOURCE = "https://bdm.insee.fr/series/sdmx/data/SERIES_BDM"
URL_STATIT = "https://api.gostatit.com/core"

out = []
keys = {}

# load maps
with open(METAMAP, "r") as i:
    metamap = json.load(i)
with open(UNITSMAP, "r") as i:
    unitmap = json.load(i)
with open(FREQUENCIESMAP, "r") as i:
    freqmap = json.load(i)

with open(KEYS, "r", encoding='utf-8') as i:
    for row in csv.reader(i):
        keys[row[0]] = row[1]


for key in keys:
  
    url = f"{URL_SOURCE}/{key}"

    r = requests.get(url)
    resp = xmltodict.parse(r.text)
