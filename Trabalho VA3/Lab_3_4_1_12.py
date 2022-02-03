class Timer:
    def __init__(self, horas = 0, minutos = 0, segundos = 0):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos

    def __str__(self):
        return f'{str(self.__horas).zfill(2)}:{str(self.__minutos).zfill(2)}:{str(self.__segundos).zfill(2)}'

    def next_second(self):
        self.__segundos += 1
        if self.__segundos >= 60:
            self.__segundos = 0
            self.__minutos += 1
        if self.__minutos >= 60:
            self.__minutos = 0
            self.__horas += 1
        if self.__horas >= 23:
            self.__horas = 0

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos < 0:
            self.__segundos = 59
            self.__minutos -= 1
        if self.__minutos < 0:
            self.__minutos = 59
            self.__horas -=1
        if self.__horas < 0:
            self.__horas = 23


timer = Timer(9, 0,0)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
