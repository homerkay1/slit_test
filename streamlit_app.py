import streamlit as st
import pandas as pd
from io import StringIO

import pytesseract
import shutil
import os
import random
from PIL import Image

st.write('This is Auto Doc Detection for Mortgage Lenders')

# TODO does this load on first use? 
uploaded_files = st.file_uploader("Choose a .png or .jpg file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    # TODO Check for PDF Version Type
    extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file))
    print(extractedInformation)
    st.write(extractedInformation)
    st.write('Doneee')
    # TODO Connect to hugchat to interpret data

