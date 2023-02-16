import web3.eth
from web3 import Web3
from Basic_02_connect import w3

def get_account_balance(address):
    balance = w3.eth.get_balance(address)
    print("This is the balance of the account: " + str(balance))
    return balance

def get_account_balance_Ether(balance):
    ether_balance = w3.fromWei(balance, 'ether')
    return ether_balance
