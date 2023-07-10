import streamlit as st
import pandas as pd
from io import StringIO

import pytesseract
import shutil
import os
import random
from PIL import Image
from hugchat import hugchat
from hugchat.login import Login

# NOTES: To Run in CodeSpaces
# streamlit run streamlit_app.py --server.enableCORS false --server.enableXsrfProtection false


st.title(":blue[**GPTDoc for Mortgage Lenders**] :100:")

st.write('**Upload your documents here for mortage automation**')

# TODO does this load on first use? 
uploaded_files = st.file_uploader("Choose a .png or .jpg file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    # TODO Check for PDF Version Type
    extractedInformation = pytesseract.image_to_string(Image.open(uploaded_file))
    st.write('Here is the Data From:' + str(uploaded_file))
    st.write(extractedInformation)
    st.write('Done')
    # TODO Connect to hugchat to interpret data
    # TODO "shareConversationsWithModelAuthors": "false",
    # TODO VERIFY THIS IS TRULY USING THIS FALSE METHOD.  SIMPLE PRINT STATEMENT MIGHT DO.
    email = 'homerkay1@gmail.com'
    passwd = 'Sharebill123'
    # TODO Make this API protected

    # Log in to huggingface and grant authorization to huggingchat
    sign = Login(email, passwd)
    cookies = sign.login()

    # Save cookies to usercookies/<email>.json
    # sign.saveCookies()
    sign.saveCookiesToDir()


    # Create a ChatBot
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict())  # or cookie_path="usercookies/<email>.json"
    # st.write(chatbot.chat("HI"))

    # Create a new conversation
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    # Get conversation list
    conversation_list = chatbot.get_conversation_list()

    while True:
        try:
            user_input # Checks if user_input alraedy defined.  If not uses this as first pass
            user_input = input('> ')
        except:
            user_input = 'This is text extracted from a document.  What type of document is it?  And what information can you find?  Any data you find please list out line by line:' + '\n' + '\n' + '"' + extractedInformation + '"'

        if user_input.lower() == '':
            pass
        elif user_input.lower() in ['q', 'quit']:
            break
        elif user_input.lower() in ['c', 'change']:
            st.write('Choose a conversation to switch to:')
            st.write(chatbot.get_conversation_list())
        elif user_input.lower() in ['n', 'new']:
            st.write('Clean slate!')
            id = chatbot.new_conversation()
            chatbot.change_conversation(id)
        else:
            st.write(chatbot.chat(user_input))

# TODO 
# Documents we will need to load and read: 
# Tax Returns
# Pay stubs, W-2s, or Other proof of income
# Bank statements and other assets
# Credit reports
# Gift letter? <- Probably don't need this one. 
# Photo ID
# Renting History

