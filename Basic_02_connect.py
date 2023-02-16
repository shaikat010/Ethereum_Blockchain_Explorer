import web3.eth
from web3 import Web3

#connecting to a node
eth = 'https://mainnet.infura.io/v3/3beb35814f274c01996224de0c825f95'
eth = 'HTTP://127.0.0.1:7545'

w3 = Web3(Web3.HTTPProvider(eth))
print("This the status of your connection to the blockchain: " + str(w3.isConnected()))

def make_connection():
    # connecting to a node
    eth = 'https://mainnet.infura.io/v3/3beb35814f274c01996224de0c825f95'
    eth = 'HTTP://127.0.0.1:7545'

    w3 = Web3(Web3.HTTPProvider(eth))
    print("This the status of your connection to the blockchain: " + str(w3.isConnected()))
    return w3

def get_latest_block_time():
    # Getting information about the latest block -------------------------------------------------
    latest_block = w3.eth.get_block('latest')
    print(latest_block)
    # Traversing or iterating over the latest block
    print("These are the latest block information ------>")
    for i, j in latest_block.items():
        print(i, j)
    return latest_block['timestamp']

def get_latest_block_number():
    latest_block = w3.eth.get_block('latest')
    return latest_block['number']

def get_own_hash():
    latest_block = w3.eth.get_block('latest')
    return latest_block['hash']

def get_latest_parent_hash():
    latest_block = w3.eth.get_block('latest')
    return latest_block['parentHash']

