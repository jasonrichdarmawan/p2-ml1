import streamlit as st
from helpers import query, plot
from PIL import Image

st.set_page_config(
    page_title='Telkomsel - PredictorTelkomsel',
    layout='wide',
    initial_sidebar_state='expanded'
)

def run():
    st.title('Telkomsel Customers Exploratory Data Analysis')
    
    st.subheader('Exploratory Data Analysis of Telkomsel Customers')
    
    st.write("This page is made by Jason Rich Darmawan Onggo Putra")
    
    st.write("Disclaimer: the data set used is not real.")
    
    df = query.fetch_all_data()
    
    st.write("## Histogram of categorical features")
    st.pyplot(fig=plot.plot_categorical_features(df=df))
    
    st.write("## Pairplot of numerical features")
    st.pyplot(fig=plot.plot_numerical_features(df))
    
    st.write("## Model Layers")
    image = Image.open("./images/sequential_improved_model.png")
    st.image(image, caption='Sequential Improved Model')
    
    st.write("## Model Strengths and Weaknesses")
    image = Image.open("./images/sequential_improved_prediction.png")
    st.image(image, caption='Sequential Improved Model Strengths and Weaknesses')
    
    st.markdown(
        """
        We will inform management, to use this model for a specific customer segment which is more predictable, according to the model:
        1. A customer with one year or two year contract.
        2. An old customer / customer with tenure above 40 / customer with total charges above 4000.
        3. A customer without internet service.
        4. A customer with internet service is unpredictable. 

           However, a customer with internet service and 1 related internet service will make the customer more predictable.
           
           e.g A customer with tech support / online security / online backup.

        5. A customer that pays with Bank Transfer (automatic)
        6. A customer with monthly charges below 20.

        We will also inform management, not to use this model for a specific customer segment, which is less predictable according to the model:
        1. A customer that is paying with Electronic check / Mail check / Credit Card (automatic).
        """
    )