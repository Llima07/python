'''
Luan Gomes de Lima
'''

import random

for _ in range(10):
    nove_digitos = ''
    for i in range(9):
        nove_digitos += str(random.randint(0, 9))

    contador_regressivo_1 = 10
    resultador_digito_1 = 0


    #validação do primeiro Digito
    for digito_1 in nove_digitos:
        resultador_digito_1 += int(digito_1) * contador_regressivo_1
        contador_regressivo_1 -= 1
    #calculos primeiro digito     
    primeiro_validador = ((resultador_digito_1 * 10) % 11)
    primeiro_validador = primeiro_validador if primeiro_validador <= 9 else 0

    #validação do segundo Digito 
    dez_digitos = nove_digitos + str(primeiro_validador)
    contador_regressivo_2 = 11
    resultador_digito_2 = 0

    for digito_2 in dez_digitos:
        resultador_digito_2 += int(digito_2) * contador_regressivo_2
        contador_regressivo_2 -= 1

    segundo_validador = ((resultador_digito_2 * 10) %  11)
    segundo_validador = segundo_validador if segundo_validador <= 9 else 0

    cpf_gerado = f'{nove_digitos}{primeiro_validador}{segundo_validador}'

    print(f'CPF: {cpf_gerado}')
