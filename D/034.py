sal = float(input(' Digite o valor do seu salário: '))

if sal >= 1250:
    valor = (sal * 10/100) + sal
else:
    valor = (sal * 15/100) + sal
print('Seu novo salario é: {:.2f}'.format(valor))
