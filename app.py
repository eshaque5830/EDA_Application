import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
# from pandas_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

#Title of web app
st.markdown('''
# **Exploratory Data Analysis Web Application**
This web application is developed by M.Ishaque called **EDA App**
''')

#Upload a file from PC
with st.sidebar.header("upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("upload your file", type=["csv"])
    df = sns.load_dataset('titanic')
    st.sidebar.markdown("[Example CSV file](https://github.com/dataprofessor/data/blob/master/iris.csv)")

#profiling report for pandas
if uploaded_file is not None:
    @st.cache
    def load_csv():
        csv = pd.read_csv(uploaded_file)
        return csv
    df =load_csv()
    pr = ProfileReport(df, explorative= True)
    st.header('**Input DF**')
    st.write(df)
    st.write('---')
    st.header('**Profiling Report with Pandas**')
    st_profile_report(pr)
else:
    st.info('Awaiting for CSV file, upload the csv')
    if st.button('Press to use example data'): #EXAMPLE dataset
        @st.cache
        def load_data():  #(col,rows)
            a = pd.DataFrame(np.random.rand(100,5),
                                columns=['age', 'banana', 'code', 'ear'])
            return a
        df =load_csv()
        pr = ProfileReport(df, explorative= True)
        st.header('**Input DF**')
        st.write(df)
        st.write('---')
        st.header('**Profiling Report with Pandas**')
        st_profile_report(pr)
