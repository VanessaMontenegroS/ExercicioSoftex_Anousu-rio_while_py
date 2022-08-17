#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre
# 1922 e 2021. A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou,
# ou completará, no ano atual (2022).
#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro
# e continuará perguntando até que um valor correto seja preenchido.

ok = False

while (ok == False):

    try:
        nome = str(input('Digite seu nome completo:\n'))
        print(' ')
        ano = int(input('Digite seu ano de nascimento:\n'))
        idade = 2022 - ano

        if ano >= 1922 and ano <= 2021:
            print(' ')
            print(f'{nome} tem:', idade, 'anos.')
            break

        else:
            print(f'Erro! Ano inválido!')
            print(' ')

    except (ValueError):
        print(' ')
        print('Este dado não é válido. Insira o que se pede!')
        print(' ')



