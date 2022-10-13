from brownie import accounts, SimpleStorage


def test_deploy():
    account = accounts[0]
    contract_obj = SimpleStorage.deploy({"from": account})
    initial_value = contract_obj.retrieve()
    expected_value = 0
    assert initial_value == expected_value


def test_update_store():
    account = accounts[0]
    contract_obj = SimpleStorage.deploy({"from": account})
    expected_value = 10
    contract_obj.store(expected_value, {"from": account})
    assert expected_value == contract_obj.retrieve()
