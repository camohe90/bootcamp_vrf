from brownie import VRFv2Consumer, accounts, config

def main():
    account = accounts.add(config["billeteras"]["llave"])
    vrfconsumer = VRFv2Consumer.deploy(5672,{"from":account})
    return vrfconsumer