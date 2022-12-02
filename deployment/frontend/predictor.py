import streamlit as st
import requests
import pandas as pd
import streamlit_toggle as tog
from configparser import ConfigParser

str_to_array = lambda items: [item.strip("\" ") for item in items.split(',')]

config = ConfigParser()
config.read('./config.ini')

if config['DEFAULT']['production'] == 'True':
    URL = config['PRODUCTION']['URL']
else:
    URL = config['DEVELOPMENT']['URL']
    
def run():
    st.title("TelkomselPredictor")
    
    with st.form(key='predictor'):
        customerID = st.text_input(
            label="Customer IDs, separate it with a comma"
        )
        fetch_customer_data = tog.st_toggle_switch(
            label="Fetch the customer data",
        )

        submitted = st.form_submit_button('Predict')
        
        if submitted:
            customerID_final = str_to_array(customerID)
            print("[DEBUG] customerID:", customerID_final)
            
            r = requests.post(
                URL+"/predict", 
                json={
                    "customerID": customerID_final,
                    "fetch_customer_data": fetch_customer_data
                }
            )
            
            if r.status_code == 200:
                res = r.json()
                st.dataframe(pd.DataFrame(res))
            else:
                st.write('Error with status code ', str(r.status_code))
         
# If we deploy the app, __name__ is app.       
if __name__ == '__main__':
    run()