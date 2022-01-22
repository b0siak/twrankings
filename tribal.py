import requests
import pandas as pd
import numpy as np
import csv
from datetime import datetime

strony = np.arange(0,8000,25)
header = ['[**]Ranking[||]', 'Nazwa[||]', 'Plemię[||]', 'Wynik[||]', 'Data[/**]']

with open('RANKINGI/zbieractwo'+datetime.today().strftime('%Y-%m-%d')+'.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)

for strona in strony:
    url = 'https://pl173.plemiona.pl/guest.php?screen=ranking&mode=in_a_day&offset='+str(strona)+'&type=scavenge'
    dfs = pd.read_html(url, match='Ranking')
    df = dfs[4]
    df = df.loc[df['Plemię'].isin(['AWW!', 'AWW.', 'AWW..', 'AWW!!', 'AWW,', 'AWW,,'])]
    df = df.astype(str) + '[|]'
    df['Ranking'] = '[*]' + df['Ranking'].astype(str)
    df.to_csv('RANKINGI/zbieractwo'+datetime.today().strftime('%Y-%m-%d')+'.csv',mode='a', index=False, header=False, sep = '\t')
    print(df)

with open('RANKINGI/farmienie'+datetime.today().strftime('%Y-%m-%d')+'.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f, delimiter="\t")
    writer.writerow(header)

for strona in strony:
    url = 'https://pl173.plemiona.pl/guest.php?screen=ranking&mode=in_a_day&offset='+str(strona)+'&type=loot_res'
    dfs = pd.read_html(url, match='Ranking')
    df = dfs[4]
    df = df.loc[df['Plemię'].isin(['AWW!', 'AWW.', 'AWW..', 'AWW!!', 'AWW,', 'AWW,,'])]
    df = df.astype(str) + '[|]'
    df['Ranking'] = '[*]' + df['Ranking'].astype(str)
    df.to_csv('RANKINGI/farmienie'+datetime.today().strftime('%Y-%m-%d')+'.csv',mode='a', index=False, header=False, sep = '\t')
    print(df)
