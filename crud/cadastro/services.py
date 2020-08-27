# Este codigo foi criado para possibilitar a utilização dos dados da API de geração de
# nomes aleatorios
import requests

def get_random_name():
    url = 'https://gerador-nomes.herokuapp.com/nome/aleatorio'
    request = requests.get(url)
    name = request.json()
    return name
