import os

def find(path, dir):
    os.chdir(path)
    lista = os.listdir()

    for item in lista:
        if item != dir:
            find(item, dir)
        else:
            os.chdir(item)
            print(os.getcwd())
            lista = os.chdir('..')
    lista = os.chdir('..')

find('./tree', 'python')