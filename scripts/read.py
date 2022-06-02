from brownie import VRFv2Consumer

def main():
    vrf_contract = VRFv2Consumer[-1]
    try:
        print(f"El numero aleatorio solicitado a chainlink es {vrf_contract.s_randomWords(0)}")
        print(f"Tu número de la suerte es {(vrf_contract.s_randomWords(0) % 20) + 1}")
        print(f"El numero aleatorio solicitado a chainlink es {vrf_contract.s_randomWords(1)}")
        print(f"Tu número de la suerte es {(vrf_contract.s_randomWords(1) % 20) + 1}")
    except:
        print("Debes esperar por lo menos un minuto")
    

