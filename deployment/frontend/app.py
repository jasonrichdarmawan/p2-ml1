import streamlit as st

import eda
import predictor
import proactive

navigation = st.sidebar.selectbox(
    label='Pilih Halaman',
    options=('EDA', 'Predictor', 'Proactive')
)

if navigation == 'EDA':
    eda.run()
elif navigation == 'Predictor':
    predictor.run()
elif navigation == 'Proactive':
    proactive.run()