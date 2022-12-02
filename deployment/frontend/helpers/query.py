import requests
import pandas as pd

def fetch_all_data() -> pd.DataFrame:
    URL = "http://127.0.0.1:5000/query"
    r = requests.get(URL)
    
    if r.status_code == 200:
        res = r.json()
        return pd.DataFrame(res)
    else:
        return ('Error with status code ', str(r.status_code))