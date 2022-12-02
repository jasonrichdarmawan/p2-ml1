import requests
import pandas as pd
from configparser import ConfigParser

config = ConfigParser()
config.read('./config.ini')

if config['DEFAULT']['production'] == 'True':
    URL = config['PRODUCTION']['URL']
else:
    URL = config['DEVELOPMENT']['URL']

def fetch_all_data() -> pd.DataFrame:
    r = requests.get(URL+"/query")
    
    if r.status_code == 200:
        res = r.json()
        return pd.DataFrame(res)
    else:
        return ('Error with status code ', str(r.status_code))