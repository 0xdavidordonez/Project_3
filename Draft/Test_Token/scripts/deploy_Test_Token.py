import os                                                    # To load key.env correctly
from dotenv import load_dotenv                               # to deploy the smart contract correctly
from brownie import accounts, config, Test_Token, network

def main():
    # Retrieve the account from the configuration
    account = accounts.add(os.getenv("private_key"))

    # Deploy the ERC20 token contract
    erc20 = Test_Token.deploy({"from": account})
    print("Token deployed at address:", erc20.address)