from os import strerror

nome_arquivo = input('Informe o nome do arquivo a ser lido: ')

arquivo = open(nome_arquivo, 'rt')
notas = dict()
try:
    for linha in arquivo:
        chave = linha.split()[0] + " " + linha.split()[1]
        notas[chave] = notas.get(chave,0) + float(linha.split()[2])

except IOError as e:
    print('I/O error ocurred: ', strerror(e.errno))

for chave in (sorted(notas.keys())):
    print(f'{chave} {notas[chave]}')



