n = input("digite algo: ")
print(type(n))
print('é um numero: ', n.isnumeric())
print('é um caractere: ', n.isalpha())
print('é alfabeticonumerico: ', n.isalnum())
print('é um caractere com espaco: ', n.isspace())
print('Todos caracteres minusculos: ', n.islower())
print('Todos caracteres maiusculo: ',n.isupper())
print('Aceita perimetros: ', n.isprintable())
