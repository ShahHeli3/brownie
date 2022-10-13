import os

from brownie import SimpleStorage, accounts


def read():
    contract_obj = SimpleStorage[-1]
    return contract_obj.retrieve()


def transact(value):
    account = accounts.add(os.getenv("PRIVATE_KEY"))
    contract_obj = SimpleStorage[-1]
    contract_obj.store(value, {"from": account})


def main():
    print(f"INITIAL VALUE: {read()}")
    transact(10)
    print(f"UPDATED VALUE: {read()}")

