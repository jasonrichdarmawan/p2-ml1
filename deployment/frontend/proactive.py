import streamlit as st

from helpers import query

def run():
    st.title('TelkomselProactive')
    
    st.write("Duly noted: The data set is not real.")
    
    st.markdown(
        """
        Telkomsel employee can use this page to get a list of customer that is going to churn.
        
        By having this list, Telkomsel will be able to proactively go to the customer, that is about to churn, and prevent that said customer from opting out of the Telco services.
        
        The list is generated with this logic:
        1. We don't have the future data set (the ones without Churn column).
        2. So just imagine that the data set we are using is connected to the database. Thus, we use the latest data.
        3. The back end fetch 10 sample and will predict whether a customer will churn or not.
        4. The back end will only return the list of customer that will churn.
        """
    )
    
    if st.button(label='Fetch new list'):
        df = query.proactive()
        st.dataframe(df)
    
    