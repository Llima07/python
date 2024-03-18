
#importações
import re
import sys

#Solicitação ao usuario
entrada = input('Digite o CPF, apenas Digitos: ')
cpf_enviado = re.sub(
    r'[^0-9]',
    '',
    entrada
)
nove_digitos = cpf_enviado[:9]

entrada_e_sequencial = entrada == entrada[0] * len(entrada)
if entrada_e_sequencial:
    print('Voce enviou dados sequenciais.')
    sys.exit()

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
dez_digitos = cpf_enviado[:9] + str(primeiro_validador)
contador_regressivo_2 = 11
resultador_digito_2 = 0

for digito_2 in dez_digitos:
    resultador_digito_2 += int(digito_2) * contador_regressivo_2
    contador_regressivo_2 -= 1

segundo_validador = ((resultador_digito_2 * 10) %  11)
segundo_validador = segundo_validador if segundo_validador <= 9 else 0

novo_cpf = f'{nove_digitos}{primeiro_validador}{segundo_validador}'

if novo_cpf == cpf_enviado:
    print(f'{cpf_enviado} é valido')
else:
    print(f'{cpf_enviado} é invalido')
