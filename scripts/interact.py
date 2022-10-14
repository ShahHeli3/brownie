# require WEB3_INFURA_PROJECT_ID variable set in your .env file
import os

from brownie import Contract, accounts


def contract_details(contract):
    name = contract.name()
    symbol = contract.symbol()
    decimals = contract.decimals()
    owner = contract.owner()
    print(f"Name: {name}")
    print(f"Symbol: {symbol}")
    print(f"Decimals: {decimals}")
    print(f"Contract Owner: {owner}")


def get_balance(contract, address):
    return contract.balanceOf(address)


def transfer_token(contract, amount):
    decimal = contract.decimals()

    # get the account addresses from .env
    sender = os.getenv("ADDRESS1")
    receiver = os.getenv("ADDRESS2")

    # get the initial balance
    print(f"\nInitial Balance \nSender: {get_balance(contract, sender)} \nReceiver: {get_balance(contract, receiver)}")

    # get the account from its private key stored in .env file
    account = accounts.add(os.getenv("PRIVATE_KEY"))

    # transfer the amount
    contract.transfer(receiver, amount * (10 ** decimal), {"from": account})

    # get the updated balance
    print(f"\nUpdated Balance \nSender: {get_balance(contract, sender)} \nReceiver: {get_balance(contract, receiver)}")


def main():
    # get the contract object
    contract_obj = Contract("0xd6409Ed3bF1E8bC9Afa03b50264441b0A221E9cd")

    # get the contract details
    contract_details(contract_obj)

    # transfer amount
    transfer_token(contract_obj, 10000000)
