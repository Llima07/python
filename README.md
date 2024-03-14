''' Calculadora com While'''

while True:
    #Variaveis de solicitação
    numero_1 = input("Digite um Numero: ")
    numero_2 = input("Digite um Numero: ")
    operador = input("Operador (+-*/): ")

    numeros_validos = None

    num_1_float = 0
    num_2_float = 0

    #conversão e validação dos numeros digitados
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None

    if numeros_validos is None:
        print('Você digitou um ou mais digitos invalidos')
        continue

    #Validação do operador digitado
    operador_permitido = '+-*/'
    if operador not in operador_permitido:
        print('Operador invalido.')
        continue
    if len(operador) > 1:
        print("Digite apenas um operador.")
        continue 

    #Operações 
    if operador == '+':
        print(f'{num_1_float} + {num_2_float} = {num_2_float + num_2_float}')
    elif operador == '-':
        print(f'{num_1_float} - {num_2_float} = {num_2_float - num_2_float}') 
    elif operador == '*':
        print(f'{num_1_float} * {num_2_float} = {num_2_float * num_2_float}')
    elif operador == '/':
        print(f'{num_1_float} / {num_2_float} = {num_2_float / num_2_float}')
    else:
        print("SE VOCE CHEGOU AQUI DEU RUIM, ME AVISE")

    #Opção de sair ou continuar
    sair = input('Desejar sair? [s]im: ').lower().startswith('s')

    if sair is True:
        print('Finalizado, até a próxima')
        break

