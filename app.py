import numpy as np
import pandas as pd
import streamlit as st
import seaborn as sns
from pandas_profiling import ProfileReport

from streamlit_pandas_profiling import st_profile_report

#Title of web app
st.markdown('<h1 style="text-align:center;">Exploratory Data Analysis Web Application</h1>', unsafe_allow_html=True)

with st.sidebar.header("Upload your dataset (.csv)"):
    uploaded_file = st.sidebar.file_uploader("upload your file", type=["csv"])
    st.sidebar.markdown("Get a data set from a GitHub repository: [Example CSV file](https://github.com/awesomedata/awesome-public-datasets)")
    
# Add another horizontal line
st.sidebar.markdown("<hr>", unsafe_allow_html=True)

st.sidebar.markdown("What is Exploratory Data Analysis (EDA)? [google](https://www.geeksforgeeks.org/what-is-exploratory-data-analysis/)")



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
    #if st.button('Press to use example data'): #EXAMPLE dataset
    if st.button('[Press to use example data from Web](https://example.com/csv_data)'): # EXAMPLE dataset    
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

  #Footer
import streamlit as st

# Your Streamlit app content

# Add some space to push the footer to the bottom
st.write("")
st.write("")

# Add your footer content with CSS
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #f5f5f5;
        padding: 10px 0;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Add your footer content
st.markdown(
    """
    <div class="footer">
        <p>Copyright © 2023 Ishaque Alidad. All rights reserved.</p>
        <p>Email: eshaquehussain@gmail.com</p>
    </div>
    """,
    unsafe_allow_html=True
)

