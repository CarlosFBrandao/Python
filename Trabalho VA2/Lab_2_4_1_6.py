#Cria o layout de todos os números
numeros = {
    '0':('###','# #','# #','# #','###'),
    '1':(' #',' #',' #',' #',' #'),
    '2':('###','  #','###','#  ','###'),
    '3':('###','  #','###','  #','###'),
    '4':('# #','# #','###','  #','  #'),
    '5':('###','#  ','###','  #','###'),
    '6':('###','#  ','###','# #','###'),
    '7':('###','  #','  #','  #','  #'),
    '8':('###','# #','###','# #','###'),
    '9':('###','# #','###','  #','###')
}

def Imprime(num):
    #Verifica se o número é válido
    try:
        if int(num) >= 0:
            # Salva cada linha em um espaço separado de uma lista
            for linha in range(len(numeros['0'])):
                lista = []
                for i in num:
                    # adiciona a linha na lista passando como parametro o número desejado contido em "números"
                    lista.append(numeros[i][linha])
                #Imprime os itens da lista separando com um espaço
                print(' '.join(lista))
        else:
            print('O número precisa ser maior que zero')
    except:
        print('Não é um número inteiro!')

num = input("Informe o número que deseja visualizar. Necessário ser inteiro e maior que zero: ")
Imprime(num)