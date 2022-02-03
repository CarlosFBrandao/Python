from calendar import Calendar

class myCalendar(Calendar):

    def count_weekday_in_year(self, year, weekday):
        self.anoDias = []
        self.contador = 0

        for i in range(1,13):
            self.anoDias.append(list(self.monthdays2calendar(year, i)))

        for meses in self.anoDias:
            for semanas in meses:

                for dia, semana in semanas:
                    if dia == 0:
                        continue
                    if semana == weekday:
                        self.contador +=1

        return self.contador

c = myCalendar()
print(c.count_weekday_in_year(2000,6))