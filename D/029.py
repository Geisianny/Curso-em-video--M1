vm = float(input('Digite a velocidade  de seu carro: '))
if vm <= 80:
    print('Você não foi multado!tenha um bom dia e dirija com segurança!')
else:
    multa = vm - 80
    print('Você foi multado! por excedeu o limite de 80 km/h, sua multa é: R${}'.format(multa*7.00))
