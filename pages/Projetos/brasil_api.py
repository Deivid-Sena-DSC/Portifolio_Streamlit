import requests

#BUSCAR CEP
def consulta_cep(cep):
    url = f"https://brasilapi.com.br/api/cep/v1/{cep}"
    resultado_cep = requests.get(url)
    return resultado_cep.text


#BUSCAR CNPJ
def consulta_cnpj(cnpj):
    url = f'https://brasilapi.com.br/api/cnpj/v1/{cnpj}'
    resultado_cnpj = requests.get(url)
    return resultado_cnpj.text

#BUSCAR FIBE
def consulta_fibe(fibe):
    url = f'https://brasilapi.com.br/api/fipe/preco/v1/{fibe}'
    resultado_fibe = requests.get(url)
    return resultado_fibe.text

print(consulta_fibe("004385-0"))