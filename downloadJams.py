import requests
import pandas as pd
import json

dfCela = pd.DataFrame()
for p in range (1, 111000, 10000):
    response = requests.get(f'https://opendata.arcgis.com/datasets/7728dfc338044352898866b8afe1a38f_0.geojson?where=objectid%20%3E%3D%20{p}%20AND%20objectid%20%3C%3D%20{p+9999}')

    data = json.loads(response.text)

    df = pd.json_normalize(data,'features')
    dfCela = dfCela.append(df)

print(dfCela.shape)
dfCela.to_csv("jamsCele.csv", sep = ',', index=False)
