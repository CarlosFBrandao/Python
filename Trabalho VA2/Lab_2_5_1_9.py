#Exemplos:
#Entrada: 19991229
#Saída: 6
#Entrada: 20000101
#Saída: 4

numero = ''
total = 0
while True:
    numero = input('Informe a data de nascimento (DiaMesAno) sem espaço: ')
    if numero.isspace() or numero.isnumeric() == False or numero.find(' ') > 0 or numero == '' \
            or (numero.isnumeric() and len(numero) != 8):
        print('Número inválido!')
    else:
        break

for item in numero:
    total += int(item)
if total >= 10:
    total2 = 0
    for item in str(total):
        total2 += int(item)
    total = total2
print(total)