n = cont = soma = 0
n = int(input('Digite um número: '))
while n != 999:
    soma += n
    cont += 1
    n = int(input('Digite um número: '))
print('Fim do programa!')
print('Foram digitados {} números e a soma deles é {}.'.format(cont, soma))


