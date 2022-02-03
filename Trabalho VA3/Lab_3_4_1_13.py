class WeekDayError(Exception):
    pass


class Weeker:
    def __init__(self, day):
        self.__diasDaSemana = ['Mon', 'Thu', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        try:
            self.__selecionado = self.__diasDaSemana.index(day)
        except:
            raise WeekDayError(Exception)

    def __str__(self):
        return self.__diasDaSemana[self.__selecionado]

    def add_days(self, n):
        for i in range(0, (n + self.__selecionado),1):
            if self.__selecionado > 6:
                self.__selecionado = 0
            self.__selecionado+=1

    def subtract_days(self, n):
        for i in range(-1, (n - self.__selecionado) ,1):
            if self.__selecionado < 0:
                self.__selecionado = 6
            self.__selecionado -= 1

try:
    weekday = Weeker('Mon')
    print(weekday)
    weekday.add_days(15)
    print(weekday)
    weekday.subtract_days(23)
    print(weekday)
    weekday = Weeker('Monday')
except WeekDayError:
    print("Sorry, I can't serve your request.")
