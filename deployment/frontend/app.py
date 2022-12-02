import streamlit as st

import eda
import predictor

navigation = st.sidebar.selectbox(
    label='Pilih Halaman',
    options=('EDA', 'Predictor')
)

if navigation == 'EDA':
    eda.run()
elif navigation == 'Predictor':
    predictor.run()