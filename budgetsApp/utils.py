# gestionsApp/utils.py
import secrets

def generer_token():
    return secrets.token_hex(32)
