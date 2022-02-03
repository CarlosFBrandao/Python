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
autoRetirar.send_keys('1.99')

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


def Cataloga():
    catalogacao = []
    resultado1 = Resultado()
    while True:
        resultado2 = Resultado()
        if resultado1 != resultado2:
            resultado1 = resultado2
            catalogacao.append(resultado1)

        if (len(catalogacao) > 1000):
            log = open('log.txt', 'a')

            for result in catalogacao:
                imp = str(imprime(result))
                log.write(imp)

            log.close()
            break

time.sleep(3)
primeiroResult = float(Resultado())
saldoInicial = float(SaldoConta())
print('Saldo Inicial:', saldoInicial)

imprime(primeiroResult)

threading.Thread(target=Cataloga).start()

while True:
    segundoResult = float(Resultado())
    if primeiroResult != segundoResult:
        primeiroResult = segundoResult
        imprime(primeiroResult)

    #se o resultado for branco, espera o verde
    if primeiroResult < 2:
        perda = 0
        para = 0
        x = 1
        while True:
            segundoResult = float(Resultado())

            if primeiroResult != segundoResult:
                primeiroResult = segundoResult
                imprime(primeiroResult)

                if primeiroResult >= 2:
                    if perda >= 1:
                        time.sleep(2)
                        comecarJogo.click()

                        while True:
                            segundoResult = float(Resultado())

                            if primeiroResult != segundoResult:
                                primeiroResult = segundoResult
                                imprime(primeiroResult)
                                if primeiroResult >= 2:
                                    print('\nGAIN')
                                    valorEntrada.send_keys(entrada)
                                    para = 1
                                if primeiroResult < 2:
                                    print('\nLOSS')
                                    btnMultiplica.click()


                                total = float(SaldoConta()) - saldoInicial
                                break
                            time.sleep(1)

                    else:
                        while True:
                            segundoResult = float(Resultado())
                            if primeiroResult != segundoResult:
                                primeiroResult = segundoResult
                                imprime(primeiroResult)
                                if primeiroResult >= 2:
                                    para = 1
                                    break

                                if primeiroResult < 2:
                                    perda += 1
                                    break

                            time.sleep(1)
            if para == 1:
                break
            if total <= stopLoss or total >= stopGain:
                break
            time.sleep(1)

    if total <= stopLoss or total >= stopGain:
        saldo = float(SaldoConta())
        if saldo > saldoInicial:
            print('Stop Gain atingido', saldo)
        else:
            print('Stop Loss atingido', saldo)
        break

    time.sleep(3)


def SegundaEstrategia():
    result = Resultado()
    while True:
        qtdLoss = 0
        resultado2 = Resultado()
        if result != resultado2:
            result = resultado2
            btnEntrar.click()

            while True:
                resultado2 = Resultado()
                if result != resultado2:
                    result = resultado2

                    if result < 1.10:
                        print('LOSS')




navegador.close()

