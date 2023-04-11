import urllib.request, json 
import pandas as pd
from pandas.io.json import json_normalize

df = pd.DataFrame()
cpf = 12345678900

for i in range(0, 1029):
    try:    
        with urllib.request.urlopen('https://api-checkin.athletico.com.br/pesquisar-cpf?cpf={}&evento={}'.format(cpf, i)) as url:
            data = json.loads(url.read().decode())
            data = pd.DataFrame(json_normalize(data, 'contratos'))
            try:
                checkin = data['checkin.status']
            except:
                print(i)
                continue
            if checkin.iloc[0] == "a":
                df = df.append(checkin, ignore_index=True)            
    except:
        print(i)
        continue

print(df)