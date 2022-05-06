#Contador de números negativos
print('Bem-vinde ao Contador de Números Negativos!\n')
quantidade = int(input('Quantos números você deseja informar? '))
contador = 0
contadorN = 0

while contador < quantidade:
    contador = contador + 1
    numeros = int(input(f'Digite o {contador}º valor:'))
    if numeros < 0:
        contadorN = contadorN + 1

print(f'\nVocê digitou {contadorN} números negativos.')
print('\nObrigade por utilizar o Contador de Números Negativos!')