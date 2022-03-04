from brownie import config, network, FundMe, MockV3Aggregator, accounts
from scripts.helpful_scripts import get_accounts, deploy_mocks

def deploy_fundme():
    account = get_accounts()

    if network.show_active() != "development":
        price_feed = config["networks"][network.show_active()]["eth_usd_price_feed"]

    else:
        deploy_mocks()
        price_feed = MockV3Aggregator[-1].address
    
    fund_me = FundMe.deploy(
        price_feed,
        {"from": account},
        publish_source=config["networks"][network.show_active()]["publish_source"]
    )   

def main():
    deploy_fundme()