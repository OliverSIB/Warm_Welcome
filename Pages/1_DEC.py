import streamlit as st
import pandas as pd

fp = r"C:\Users\OliverHughes\OneDrive - Social Investment Business\Desktop\Other\Elisha\WW Data.xlsx"
wwdf = pd.read_excel(fp, sheet_name='Clean Warm Spaces w IMD UR')
epcdf = pd.read_excel(fp, sheet_name='EPC Certificates')
decdf = pd.read_excel(fp, sheet_name='DEC Certificates')




st.write(decdf)