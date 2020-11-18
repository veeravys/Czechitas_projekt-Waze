import requests
import pandas as pd
import json


dfCela = pd.DataFrame()
for p in range (1, 90000, 10000):
    response = requests.get(f'https://opendata.arcgis.com/datasets/5c6a2f3f86ac49d2b2ab21a837667e85_0.geojson?where=objectid%20%3E%3D%20{p}%20AND%20objectid%20%3C%3D%20{p+9999}')

    #data = json.loads(response.text) nebo jednodusseji:
    data = response.json()
    df = pd.json_normalize(data,'features')
    dfCela = dfCela.append(df)

dfCela.to_csv('alertsCele.csv', sep = ',', index = False)

