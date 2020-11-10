dist = float(input('Digite a distancia da viagem: '))
if dist <= 200:
    valor = dist * 0.50
    print('O preço de sua passagem é: {:.2f}'.format(valor))
else:
    valor = dist * 0.45
    print('O preço de sua passagem é: {:.2f}'.format(valor))
