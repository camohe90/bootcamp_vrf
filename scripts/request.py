from brownie import VRFv2Consumer, accounts, config

def main():
    account = accounts.add(config["billeteras"]["llave"])
    vrf_contract = VRFv2Consumer[-1]
    print(vrf_contract)
    try:
        tx = vrf_contract.requestRandomWords({"from":account})
        tx.wait(1)
    except:
        print("Recuerda por favor agregar fondos a tu subscripción")
        return 
    print("Hice la solicitud")