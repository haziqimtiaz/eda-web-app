#eda web app using streamlit and pandas profiling
import streamlit as st
import pandas as pd
from pandas_profiling import ProfileReport
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_pandas_profiling import st_profile_report
st.markdown('''
# EDA Web App
##### Made by: [Haziq Imtiaz](https://github.com/haziqimtiaz)
This app performs Exploratory Data Analysis on **csv** files!
***
''')
st.sidebar.header('User Input Features')
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
    st.header('**Input DataFrame**')
    st.write(input_df)
    profile = ProfileReport(input_df, explorative=True)
    st.header('**Pandas Profiling Report**')
    st_profile_report(profile)
else:
    st.info('Awaiting for CSV file to be uploaded.')
    if st.button('Press to use Example Dataset'):
        # titanic
        titanic=sns.load_dataset('titanic')
        st.header('**Titanic Dataset**')
        st.write(titanic)
        profile = ProfileReport(titanic, explorative=True)
        st.header('**Pandas Profiling Report**')
        st_profile_report(profile)
    