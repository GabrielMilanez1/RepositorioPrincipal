repetir = 1
while repetir != 0:
    print('Bem vindo ao programa "OrigemIMEI"!\n\nPara começar, digite "*#06#" em seu celular para descobrir o número IMEI. Após isso:')
    imei = str(input('\nDigite aqui o seu numero IMEI para a consulta (somente os 15 primeiros números): '))
    while type(imei) != int:
        if imei.isdigit() == True and len(imei) == 15:
            break
        else:
            imei = str(input('Você deve digitar apenas em números e os primeiros 15 digitos de seu IMEI. Escreva novamente: '))

    print('\n\nInformações sobre o IMEI "{}/{}/{}".'.format(imei[0:6], imei[6:8], imei[8:15]))
    fs = 'O dispositivo pertencente ao IMEI informado'

    if imei[6:8] == '00':
        print('{} foi fabricado na fábrica original de sua marca.'.format(fs))
    elif imei[6:8] == '06' or imei[6:8] == '08' or imei[6:8] == '78':
        print('{} foi fabricado na Alemanha.'.format(fs))
    elif imei[6:8] == '07':
        print('{} pode ter sido fabricado na Alemanha ou Coreia do Sul.'.format(fs))
    elif imei[6:8] == '13':
        print('{} foi fabricado no Azerbaijão.'.format(fs))
    elif imei[6:8] == '05' or imei[6:8] == '50':
        print('{} pode ter sido fabricado no Brasil, Estados Unidos ou Finlândia.'.format(fs))
    elif imei[6:8] == '03' or imei[6:8] == '49' or imei[6:8] == '81' or imei[6:8] == '92' or imei[6:8] == '93':
        print('{} foi fabricado na China.'.format(fs))
    elif imei[6:8] == '80':
        print('{} pode ter sido fabricado na China, Alemanha ou Hungria.'.format(fs))
    elif imei[6:8] == '11':
        print('{} pode ter sido fabricado na China ou Vietnam.'.format(fs))
    elif imei[6:8] == '18' or imei[6:8] == '80':
        print('{} foi fabricado em Cingapura.'.format(fs))
    elif imei[6:8] == '30':
        print('{} foi fabricado na Coreia do Sul.'.format(fs))
    elif imei[6:8] == '02':
        print('{} pode ter sido fabricado na Coreia do Sul ou nos Emirados Árabes Unidos.'.format(fs))
    elif imei[6:8] == '20':
        print('{} foi fabricado nos Emirados Árabes Unidos.'.format(fs))
    elif imei[6:8] == '40' or imei[6:8] == '41':
        print('{} foi fabricado na Escócia.'.format(fs))
    elif imei[6:8] == '67':
        print('{} foi fabricado nos Estados Unidos.'.format(fs))
    elif imei[6:8] == '01' or imei[6:8] == '10' or imei[6:8] == '70' or imei[6:8] == '91':
        print('{} foi fabricado na Finlândia.'.format(fs))
    elif imei[6:8] == '04':
        print('{} pode ter sido fabricado na Hungria ou na China.'.format(fs))
    elif imei[6:8] == '09':
        print('{} foi fabricado na Índia.'.format(fs))
    elif imei[6:8] == '19':
        print('{} foi fabricado na Inglaterra.'.format(fs))
    elif imei[6:8] == '71':
        print('{} foi fabricado na Malásia.'.format(fs))
    elif imei[6:8] == '44':
        print('{} foi fabricado no Reino Unido.'.format(fs))
    else:
        print('Não foi possível realizar a consulta, verifique o IMEI digitado e tente novamente (não consta em nosso banco de dados).')
    
    pergunta = str(input('\nVocê deseja consultar mais um número de IMEI? digite (1) para sim e (0) para não: '))
    while type(pergunta) != int:
        if pergunta.isdigit() == True and int(pergunta) <= 1:
            perguntaNUM = int(pergunta)
            break
        else:
            pergunta = str(input('Você deve apenas digitar "1" ou "0". Tente novamente: '))
    if perguntaNUM == 0:
        repetir = repetir - 1
        print('\nFim de operação.')

#https://github.com/GabrielMilanez1
