import os

from brownie import accounts, SimpleStorage


def deploy_simple_storage():
    account = accounts.add(os.getenv("PRIVATE_KEY"))

    # deploy and create a contract object
    contract_obj = SimpleStorage.deploy({
        "from": account
    })

    # call
    # initial_value = contract_obj.retrieve()
    # print(f"INITIAL: {initial_value}")
    #
    # # transact
    # transaction = contract_obj.store(10, {"from": account})
    # transaction.wait(1)
    #
    # updated_value = contract_obj.retrieve()
    # print(f"UPDATED: {updated_value}")


def main():
    deploy_simple_storage()
