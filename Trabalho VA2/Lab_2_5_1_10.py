#Exemplo:
#Entrada: donor / Nabucodonosor
#Saída:Yes
#Entrada: donut / Nabucodonosor
#Saída: No

palavra1 = input('Informe a primeira palavra: ')
palavra2 = input('Informe a segunda palavra: ')
resultado = False
for letra in palavra1.upper():
    if palavra2.upper().find(letra) >= 0:
        resultado = True
    else:
        resultado = False
        break
print('Yes') if resultado else print('No')