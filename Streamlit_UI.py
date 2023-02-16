import streamlit as st
from Basic_02_connect import get_latest_block_time,get_latest_block_number, get_own_hash,get_latest_parent_hash,make_connection
from Basic_02_native import get_account_balance, get_account_balance_Ether

# import Image from pillow to open images
from PIL import Image

img = Image.open("Ethereum.png")
# display image using streamlit
# width is used to set the width of an image to be set


col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(img, width=200)

with col3:
    st.write(' ')


st.markdown("<h1 style='text-align: center; color: orange;'>  Ethereum Blockchain Explorer </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: left; color: white;'>Ethereum Blockchain Explorer</h3>", unsafe_allow_html=True)


if st.button('Connect to Local Blockchain'):
    result = make_connection()
    st.success("Connected to the local blockchain!")

if st.button('Check Connected Port'):
    result = 'HTTP://127.0.0.1:7545'
    st.success(result)

if st.button('Check Latest Block Time'):
    result = get_latest_block_time()
    st.success(result)


if st.button('Check Latest Block Number'):
    result = get_latest_block_number()
    st.success(result)


if st.button('Check Latest Block Hash'):
    result = get_own_hash()
    st.success(result)

if st.button('Check Current Block Parent'):
    result = get_latest_parent_hash()
    st.success(result)

Address = st.text_input("Account Address", "Type Here ...")
if st.button('Get Account Balance in Wei'):
    balance = get_account_balance(Address)
    st.success(balance)

if st.button("Get balance in Ether"):
    balance = get_account_balance(Address)
    balance_Ether = get_account_balance_Ether(balance)
    st.success(balance_Ether)

with st.sidebar:
    img = Image.open("eth_logo.png")
    st.header("What is a Blockchain Explorer? ")
    st.image(img, width=200)
    st.write("Block explorers are one of the most important tools in a crypto enthusiast’s arsenal. They provide an online interface for searching a blockchain, and enable you to retrieve data about transactions, addresses, blocks, fees, and more. Each block explorer provides data about a particular blockchain, and the type of information included will vary depending on the architecture of the blockchain it serves.")