"""Подключаемые модули"""
import datetime as dt                                                  #Подключили библиотеку времени




"""Родительский класс для калькуляторов"""
class Calculator:
    today = dt.datetime.now().date()                                   #Установили текущее время
    the_cost = 0                                                       #Создали счетчик с первым значением 0

    def __init__(self, limit):                                         #Создали калькулятор со свойствами: лимит
        self.limit = limit
        self.records = []                                              #Создали пустой список в свойствах   

    def add_record(self, record):                                      #Метод добавления объекта класса Record в список records[]
        self.records.append(record)

    def get_today_stats(self):                                         #Метод подсчета трат за сегодня
        for object in self.records:                                    #Прошлись циклом по списку
            if object.date == self.today:                              #Выделили объекты с необходимой датой
                self.the_cost = self.the_cost + object.amount          #Добавили сумму в счетчик
        return self.the_cost       
    
    def get_week_stats(self):
        for object in self.records:                                    #Прошлись циклом по списку
            if object.date >= self.today - dt.timedelta(days=7):       #Определили временные рамки
                self.the_cost = self.the_cost + object.amount          #Добавили сумму в счетчик
        return self.the_cost




"""Класс для записей"""
class Record:
    today = dt.datetime.now().date()                                    #Установили текущее время
    def __init__(self, amount, comment, date = None):
        self.amount = amount
        self.comment = comment
        if date == None:                                                #Если аргумент date ничего не содержит - принять текущее время
            self.date = self.today
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()   #Иначе преобразовать в заданный формат




"""Дочерний класс для CASH калькулятора"""
class CashCalculator(Calculator): 
    USD_RATE  = 73.18
    EURO_RATE = 81.86
    def get_today_cash_remained(self, currency):  
        if currency == "usd":
            self.currency = self.USD_RATE
            self.name_currency = "USD"
        elif currency == "eur":
            self.currency = self.EURO_RATE
            self.name_currency = "Euro"
        else:
            self.currency = 1
            self.name_currency = "руб"

        for object in self.records:
            if object.date == self.today:
                self.limit = (self.limit - object.amount)
        
        if self.limit > 0:
            return (f"На сегодня осталось {round(self.limit/self.currency,2)} {self.name_currency}")          
        elif self.limit == 0:
            return (f"Денег нет, держись")
        else: 
            return (f"Денег нет, держись: твой долг - {abs(round(self.limit/self.currency,2))} {self.name_currency}")

        


"""Дочерний класс для Calories калькулятора"""
class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        for object in self.records:
            if object.date == self.today:
                self.limit = self.limit - object.amount
        if self.limit >= 0:
            return (f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {self.limit} кКал")
        else:
            return (f"Хватит есть!")



cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе")) 

cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))

cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("eur"))
