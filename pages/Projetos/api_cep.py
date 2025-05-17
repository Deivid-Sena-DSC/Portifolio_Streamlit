import requests

def consulta_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resultado_cep = requests.get(url)
    return resultado_cep.text