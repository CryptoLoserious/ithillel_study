# # # task_1 + task_2
"""Створіть клас "Місто". Необхідно зберігати в полях класу: назву міста, назву регіону, назву країни,
кількість жителів міста, поштовий індекс міста, телефонний код міста.
 Реалізуйте доступ до окремих полів (Інкапсуляція).
 та  Завдання 2:
Створіть клас "Країна". Необхідно зберігати в полях класу: назву країни, назву континенту, кількість жителів країни,
телефонний код країни, назву столиці, назву міст країни. Реалізуйте доступ до окремих полів (Інкапсуляція)."""

class Country:
    __population = None
    __capital = None
    cities = []
    def __init__(self, name, region, capital, population, code = None, cities = None):
        self.name = name
        self.region = region
        self.__population = population
        self.__capital = capital
        self.code = code
        self.cities = cities

    def set_pop(self, population):
        if 2 < len(population) < 50:
            self.__population = population
        else:
            print("Incorrect length of population!")
    def get_pop(self):
        return self.__population

    def set_capital(self, capital):
        if len(capital) >= 2:
            self.__capital = capital
        else:
            print("Incorrect capital length!")

    def get_capital(self):
        return self.__capital

    def get_info(self):
        print(f"name: {self.name}, region: {self.region}, capital: {self.__capital} population: {self.__population}, "
              f"code: {self.code}, cities: {self.cities}")


class City(Country):
    def __init__(self, name, region, population, code):
        super(City, self).__init__(name, region, population, code)


Ukraine = Country("Ukraine", "Europe", "Kyiv" ,"39 bill","+38",
                  "Kyiv, Kharkiv, Dnipro, Donetsk, Lugansk, Odesa"  )
Ukraine.get_info()

Kyiv = City("Kyiv", "Kyivskyi", "12 bill", "044" )
Kyiv.get_info()


