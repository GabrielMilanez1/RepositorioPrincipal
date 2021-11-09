#Timer automático para lembrar de algo durante uso de computador pessoal/profissional

import time
import pyautogui

segundos_contador = 0
minutos_contador = 0

minutos_alarme_all = str(pyautogui.prompt('Escreva a quantidade de minutos para o timer', title='Timer'))
while type(minutos_alarme_all) != int:
    if minutos_alarme_all.isdigit() == True:
        minutos_alarme = int(minutos_alarme_all)
        break
    else:
        minutos_alarme_all = str(pyautogui.prompt('Você deve inserir um número!', title='Timer'))

while minutos_alarme == 0:
    segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número! (E que seja maior que "0" já que a quantidade de minutos escolhida foi "0"', title='Timer'))
    while segundos_alarme_all.isdigit() == False: 
        segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número! (E que seja maior que "0" já que a quantidade de minutos escolhida foi "0"', title='Timer'))
        if segundos_alarme_all.isdigit() == True:
            if int(segundos_alarme_all) == 0:
                segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número! (E que seja maior que "0" já que a quantidade de minutos escolhida foi "0"', title='Timer'))
                while type(segundos_alarme_all) != int:
                    if segundos_alarme_all.isdigit() == True and int(segundos_alarme_all) > 0 and int(segundos_alarme_all) <= 59:
                        segundos_alarme = int(segundos_alarme_all)
                        break
                    else: 
                        segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número, que seja menor que 59! (E que seja maior que "0" já que a quantidade de minutos escolhida foi "0"', title='Timer'))
            else:
                while type(segundos_alarme_all) != int:
                    if segundos_alarme_all.isdigit() == True and int(segundos_alarme_all) <= 59:
                        segundos_alarme = int(segundos_alarme_all)
                        break
                    else:
                        segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número, que seja menor que 59!', title='Timer'))
    if int(segundos_alarme_all) > 0:
        segundos_alarme = int(segundos_alarme_all)
        break

while minutos_alarme != 0:
    segundos_alarme_all = str(pyautogui.prompt('Escreva a quantidade de segundos para o timer. (Apenas um número de 0 a 59)', title='Timer'))
    while segundos_alarme_all.isdigit() == False:
        segundos_alarme_all = str(pyautogui.prompt('Escreva a quantidade de segundos para o timer. (Apenas um número de 0 a 59)', title='Timer'))
        if segundos_alarme_all.isdigit() == True:
            if int(segundos_alarme_all) <= 59:
                while type(segundos_alarme_all) != int:
                    if segundos_alarme_all.isdigit() == True and int(segundos_alarme_all) <= 59:
                        segundos_alarme = int(segundos_alarme_all)
                        break
                    else:
                        segundos_alarme_all = str(pyautogui.prompt('Você deve inserir um número, que seja menor que 59!', title='Timer'))
    if int(segundos_alarme_all) >= 0:
        segundos_alarme = int(segundos_alarme_all)
        break
while segundos_contador <= 70:
    if segundos_contador == 59:
        time.sleep(1)
        segundos_contador = 0
        minutos_contador += 1
        print('{}:{}'.format(minutos_contador, segundos_contador))
    else:
        time.sleep(1)
        segundos_contador += 1
        print('{}:{}'.format(minutos_contador, segundos_contador))
    if minutos_contador == minutos_alarme and segundos_contador == segundos_alarme:
        pyautogui.press('win')
        time.sleep(0.3)
        pyautogui.write('*fim do timer*')
        break
