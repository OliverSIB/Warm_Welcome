import streamlit as st
import pandas as pd

# import data
fp = r"C:\Users\OliverHughes\OneDrive - Social Investment Business\Desktop\Other\Elisha\WW Data.xlsx"
# Warm welcome data
wwdf = pd.read_excel(fp, sheet_name='Clean Warm Spaces w IMD UR')
# epc data
epcdf = pd.read_excel(fp, sheet_name='EPC Certificates')
# dec data
decdf = pd.read_excel(fp, sheet_name='DEC Certificates')


# set titles/icon/layout ----------------------------------
st.set_page_config(page_title="Warm Welcome App", layout = 'wide')











st.title("Warm Welcome Data")

st.header('What is a dec?')
st.write("Display Energy Certificates (DECs) are designed to show the energy performance of public buildings.They use a scale that runs from ‘A’ to ‘G’ - ‘A’ being the most efficient and ‘G’ being the least.")

st.header("Validity period of DECs")
st.write("Where the building has a total useful floor area of more than 1,000m2, the DEC is valid for 12 months. The accompanying advisory report is valid for 7 years. Where the building has a total useful floor area of between 250m2 and 1000m2, the DEC and advisory report are valid for 10 years.")

st.header("I need to display a DEC – do I also need an EPC for my building?")
st.write("You will only need to have an EPC if you construct (including certain modifications), sell or let your building. If you do have an EPC for your building, the rating must be displayed on your DEC.")







# Sidebar with search functionality --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Checkbox for filtering or displaying the entire dataset
st.sidebar.header('Search the data')

# Checkbox for filtering or displaying the entire dataset
st_filter_option = st.sidebar.checkbox('Filter Space Type Data')

if st_filter_option:
    # Selectbox for Space Type
    Space_Type = st.sidebar.selectbox('Type or select Space Type', wwdf['Space Type'].unique())

    # Filter DataFrame based on selected Space Type
    filtered_df = wwdf[wwdf['Space Type'] == Space_Type]
    
    if filtered_df.empty:
        st.sidebar.error(f"Whoops: '{Space_Type}' doesn't exist in the dataset.")
else:
    # If not filtering, display the entire dataset
    filtered_df = wwdf


# Checkbox for filtering or displaying the urban_rural
ru_filter_option = st.sidebar.checkbox('Filter Rural Urban Data')

if ru_filter_option:
    # Selectbox for urban_rural
    urban_rural = st.sidebar.selectbox('Type or select Rural/Urban Classification', wwdf['urban_rural'].unique())

    # Filter DataFrame based on selected urban_rural
    filtered_df2 = wwdf[wwdf['urban_rural'] == urban_rural]
    
    if filtered_df2.empty:
        st.sidebar.error(f"Whoops: '{urban_rural}' doesn't exist in the dataset.")
else:
    # If not filtering, display the entire dataset
    filtered_df2 = filtered_df




# Checkbox for filtering or displaying the urban_rural
imd_filter_option = st.sidebar.checkbox('Filter IMD Data')

if imd_filter_option:
    # Selectbox for urban_rural
    IMD = st.sidebar.selectbox('Type or select IMD', wwdf['IMD2019 Decile'].unique())

    # Filter DataFrame based on selected urban_rural
    filtered_df3 = wwdf[wwdf['IMD2019 Decile'] == IMD
]
    
    if filtered_df3.empty:
        st.sidebar.error(f"Whoops: '{IMD}' doesn't exist in the dataset.")
else:
    # If not filtering, display the entire dataset
    filtered_df3 = filtered_df2
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------











# add an image to break up the page
st.image('Warm_Welcome_Image.jpg')

st.header("Lets explore the data")

col1, col2, col3 = st.columns((3))
# count of certs
with col1:
    num_ww = filtered_df3['ID'].nunique()
    st.write("Number of Warm Welcome Buildings", num_ww)
    both = filtered_df3[filtered_df3['Both?'] == 'Y'].shape[0]
    st.write("Number of Warm Welcome Buildings with Both EPC and DEC", both)
    neither = filtered_df3[filtered_df3['Has A Cert?'] == 'N'].shape[0]
    st.write("Number of Warm Welcome Buildings with neither EPC or DEC", neither)
with col2:
    num_epc = epcdf['ID'].nunique()
    st.write("Number of Warm Welcome Buildings with EPCs", num_epc)
    perc_epc = (num_epc/num_ww*100).__round__(1)
    st.write("Percentage of WW with EPC", perc_epc)
with col3:
    num_dec = decdf['ID'].nunique()
    st.write("Number of Warm Welcome Buildings with DECs", num_dec)
    perc_dec = (num_dec/num_ww*100).__round__(1)
    st.write("Percentage of WW with DEC", perc_dec)