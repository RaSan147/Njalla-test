from .API import NjallaAPI
from .Domain import NjallaDomain
from .Server import NjallaServer
from .User import NjallaUser
from .VPN import NjallaVPN
from .Wallet import NjallaWallet

def njalla(api_key):
    return NjallaAPI(api_key)
