#  Escreva um programa em Python que leia um número
#  inteiro qualquer e peça para o usuário escolher qual
#  será a base de conversão: 1 para binário, 2 para octal
#  e 3 para hexadecimal.

num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] - Binário
[2] - Octal
[3] - Hexadecimal''')
opcao = int(input('Sua opção: '))

if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')

#  0b = binário, 0o = octal, 0x = hexadecimal