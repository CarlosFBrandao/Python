# Caesar cipher - decrypting a message.
#exemplos: abcxyzABCxyz 123 /2
#Saída: cdezabCDEzab 123
#Exemplo: The die is cast /25
#Saída: Sgd chd hr bzrs


cipher = input('Enter your cryptogram: ')
num = input('Informe um número de deslocamento de 1 a 25: ')
while True:
    if num.isnumeric():
        if  int(num) < 1 or int(num) > 25:
            num = input('Informe um número de deslocamento de 1 a 25: ')
        else:
            num = int(num)
            break
    else:
        num = input('Informe um número de deslocamento de 1 a 25: ')
text = ''
for char in cipher:
    if not char.isalpha():
        text += char

    else:
        charOrig = char
        char = char.lower()
        code = ord(char) +num
        if code >= 123:
            code = (ord('a') +( code - 123))
        if code < ord('A'):
            code = ord('Z') +num
        if charOrig.isupper():
            letra = chr(code).upper()
        else:
            letra = chr(code)
        text += letra

print(text)