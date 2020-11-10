from random import randint
n = randint(0, 5)
print('-=-' * 10)
print(' Vou pensar em um número entre 0 e 5. tente adivinhar  ')
print('-=-'*10)
num = int(input('Em que numero eu pensei? '))
print('PROCESSANDO...')
if n == num:
    print('Parabens! vc me venceu!!!')
else:
    print('Vc errou!o numero era {} e não {}'.format(n,num))
print('========================================================')
