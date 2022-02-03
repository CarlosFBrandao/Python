from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import threading

navegador = webdriver.Chrome()
navegador.implicitly_wait(3)
navegador.get('https://blaze.com/pt/games/crash')

#valores de stop
total = 0
stopGain = 5.03
stopLoss = -1000
gale = 1
entrada = '1'

#login
btnLogin = navegador.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div/div[1]/a')
btnLogin.click()
time.sleep(1)

usuario = navegador.find_element_by_xpath('//*[@id="auth-modal"]/div[2]/form/div[1]/div/input')
senha = navegador.find_element_by_xpath('//*[@id="auth-modal"]/div[2]/form/div[2]/div/input')
btnEntrar = navegador.find_element_by_xpath('//*[@id="auth-modal"]/div[2]/form/div[4]/button')

usuario.send_keys('carlosparatrader@gmail.com')
senha.send_keys('NG@mastermaq2010')

time.sleep(1)

btnEntrar.click()

input('Login: ')
#resgatando saldo da conta
def SaldoConta():
    saldoTxt = navegador.find_element_by_xpath('//*[@id="header"]/div/div[2]/div/div[1]/div/a/div/div/div')
    saldo = saldoTxt.text
    saldo = saldo.replace('R$', '')
    print(saldo)
    saldo = float(saldo)
    return saldo

#definindo Entradas:
valorEntrada = navegador.find_element_by_xpath('//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[1]/div/div[1]/input')
autoRetirar = navegador.find_element_by_xpath('//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[2]/div[1]/input')

valorEntrada.send_keys(entrada)
autoRetirar.send_keys('1.10')

#instanciando botão Começar Jogo e X2
comecarJogo = navegador.find_element_by_xpath('//*[@id="crash-controller"]/div[1]/div[2]/div[2]/button')
btnMultiplica = navegador.find_element_by_xpath('//*[@id="crash-controller"]/div[1]/div[2]/div[1]/div[1]/button[2]')

def Resultado():
    cont = 0
    while True:
        try:
            xPatch = '//*[@id="crash-recent"]/div[2]/div[1]/span[1]'
            labResults = navegador.find_element_by_xpath(xPatch)
            primeiroResult = str(labResults.text)
            primeiroResult = primeiroResult.replace("X", "")
            primeiroResult = float(primeiroResult)
            break
        except:
            time.sleep(0.5)
            cont += 1
            if cont == 3:
                primeiroResult = 0.0
                break

    return primeiroResult

def imprime(valor):
    valorstr = str(valor)
    print('\033[31m', (valorstr+'X'), '\033[31m', end='') if valor < 2 else print('\033[32m', (valorstr+'X'), '\033[32m', end='')

saldo = SaldoConta()
result = Resultado()
imprime(result)
qtdloss = 0
while True:
    entrada2 = float(entrada)
    resultado2 = Resultado()
    if result != resultado2:
        result = resultado2
        imprime(result)

        if result <= 1.10:
            qtdloss += 1

        if result > 1.10:
            qtdloss = 0

        if qtdloss == 3:
            time.sleep(2)
            comecarJogo.click()
            while True:
                resultado2 = Resultado()
                if result != resultado2:
                    result = resultado2
                    imprime(result)

                    if result <= 1.10:
                        print('LOSS')
                        entrada2 = str(entrada2)
                        entrada2 = entrada2.replace(',', '.')
                        entrada2 = (float(entrada2) * 11)
                        entrada2 = str(entrada2)
                        entrada2 = entrada2.replace('.',',')
                        valorEntrada.send_keys(str(entrada2))
                        time.sleep(2)
                        comecarJogo.click()

                    if result > 1.10:
                        print('\033[32m','GAIN','\033[32m')
                        valorEntrada.send_keys(str(entrada))
                        total = float(SaldoConta()) - saldo
                        qtdloss = 0
                        time.sleep(1)
                        break

                time.sleep(1)

    if total >= stopGain:
        print('\033[32m', 'Stop gain atingido', '\033[32m', end='')
        print(SaldoConta())
        break
    time.sleep(1)

navegador.close()