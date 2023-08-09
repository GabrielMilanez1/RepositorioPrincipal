import requests
import pyautogui

while True:
    cep = str(pyautogui.prompt("Digite o CEP: "))
    while type(cep) == str:
        if cep.isdigit() != True or len(cep) != 8:
            cep = str(pyautogui.prompt("O CEP deve ter somente números e 8 dígitos, tente novamente: "))
        else:
            break
    cepFormatado = f'{cep[0]}{cep[1]}{cep[2]}{cep[3]}{cep[4]}-{cep[5]}{cep[6]}{cep[7]}'
    link = f'https://viacep.com.br/ws/{cep}/json/'
    try:
        requisicao = requests.get(link)
        dicionario = requisicao.json()
        pyautogui.confirm("O CEP: {} é de: {}, fica em: {} no bairo {}".format(cepFormatado, dicionario['localidade'], dicionario['logradouro'], dicionario['bairro']), title='CEP', buttons=['Ok'])
        break
    except:
        pyautogui.confirm("O CEP {} não é válido.".format(cep), title='CEP', buttons=['Ok'])
        break