import streamlit as st
import pandas as pd

fp = r"C:\Users\OliverHughes\OneDrive - Social Investment Business\Desktop\Other\Elisha\WW Data.xlsx"
wwdf = pd.read_excel(fp, sheet_name='Clean Warm Spaces w IMD UR')
epcdf = pd.read_excel(fp, sheet_name='EPC Certificates')
decdf = pd.read_excel(fp, sheet_name='DEC Certificates')

# Combine DataFrames into a single DataFrame
all_data = pd.concat([wwdf, epcdf, decdf], ignore_index=True)

# Streamlit App
st.title('Warm Welcome Search')

# User input for search using a dropdown
search_term = st.selectbox('Select ID to search:', wwdf['ID'].astype(str).unique())

# Filter dataframes based on the selected ID
wwdf_result = wwdf[wwdf['ID'].astype(str) == search_term]
epcdf_result = epcdf[epcdf['ID'].astype(str) == search_term]
decdf_result = decdf[decdf['ID'].astype(str) == search_term]

# Display results based on user input
if search_term:
    st.subheader('Clean Warm Spaces w IMD UR:')
    st.write(wwdf_result)

    st.subheader('EPC Certificates:')
    st.write(epcdf_result)

    st.subheader('DEC Certificates:')
    st.write(decdf_result)
else:
    st.info('Select an ID to search.')
