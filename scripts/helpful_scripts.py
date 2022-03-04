from brownie import accounts, config, network, MockV3Aggregator
from web3 import Web3 as w3

decimels = 18
initial_value = 2500

def get_accounts():
    if network.show_active() == "development":
        return accounts[0]

    else:
        return accounts.add(config["wallets"]["from_key"])

def deploy_mocks():
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(
            decimels, w3.toWei(initial_value, "ether"), {"from": get_accounts()}
        )