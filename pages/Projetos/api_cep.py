import requests
import json

def consulta_cep(cep):
    url = f"https://cep.awesomeapi.com.br/json/{cep}"
    resultado_cep = requests.get(url)
    return resultado_cep.text