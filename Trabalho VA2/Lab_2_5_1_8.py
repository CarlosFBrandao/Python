#teste
#Entrada: Listen / Silent
#Saída: Anagrams
#Entrada: modern/norman
#Saída: Not anagrams

anagrama = False
palavra1 = ''
palavra2 = ''

while True:
    palavra1 = input('Informe a primeira palavra: ')
    if palavra1.isspace() or palavra1 == '':
        print('Informe uma palavra válida')
        continue
    palavra2 = input('Informe a segunda palavra: ')
    if palavra2.isspace() or palavra2 == '':
        print('Informe uma palavra válida')
        continue
    else:
        palavra1 = palavra1.upper()
        palavra2 = palavra2.upper()
        break

for letra in palavra2:
    if palavra1.count(letra) > 0 and palavra1.count(letra) == palavra2.count(letra):
        anagrama = True
    else:
        anagrama = False
        break

print('É um anagrama!') if anagrama == True else print('Não é um anagrama!')