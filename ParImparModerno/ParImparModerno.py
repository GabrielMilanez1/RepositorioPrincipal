import random
import time
import pyautogui

jogar = True

numero_sorteado = random.randint(1, 10)

pyautogui.alert('Bem-vindo ao jogo "par ou ímpar"!\n',title='Par ou ímpar', button='Continuar')
while jogar:
    escolha = pyautogui.confirm('Escolha uma das opções:',title='Par ou ímpar', buttons=['Par', 'Ímpar'])

    if escolha == 'Par':
        pyautogui.alert('Você escolheu "{}".\nClique para sortear um número!'.format(escolha),title='Par ou ímpar', button='Sortear')
        time.sleep(2)
        pyautogui.alert('Número sorteado com sucesso!',title='Par ou ímpar', button='Continuar')
        if numero_sorteado % 2 == 0:
            pyautogui.alert('Você ganhou!\nO número sorteado foi: "{num}".\n"{num}" é um número par!'.format(num = numero_sorteado),title='Par ou ímpar', button='Continuar')
        else:
            pyautogui.alert('Você perdeu!\nO número sorteado foi "{num}".\n"{num}" é um número ímpar, e você escolheu: "{escolha}"!'.format(num = numero_sorteado, escolha = escolha),title='Par ou ímpar', button='Continuar')

    if escolha == 'Ímpar':
        pyautogui.alert('Você escolheu "{}".\nClique para sortear um número!'.format(escolha),title='Par ou ímpar', button='Sortear')
        time.sleep(2)
        pyautogui.alert('Número sorteado com sucesso!',title='Par ou ímpar', button='Continuar')
        if numero_sorteado % 2 == 0:
            pyautogui.alert('Você perdeu!\nO número sorteado foi: "{num}".\n"{num}" é um número par, e você escolheu: "{escolha}"!'.format(num = numero_sorteado, escolha = escolha),title='Par ou ímpar', button='Continuar')
        else:
            pyautogui.alert('Você ganhou!\nO número sorteado foi: "{num}".\n"{num}" é um número ímpar!'.format(num = numero_sorteado),title='Par ou ímpar', button='Continuar')

    pergunta = pyautogui.confirm('\nVocê deseja jogar novamente?',title='Par ou ímpar', buttons=['Sim', 'Não'])

    if pergunta == 'Não' or pergunta is None:
        pyautogui.alert('\n\nFim de jogo!',title='Par ou ímpar', button='Sair')
        jogar = False