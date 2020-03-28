import datetime as dt                                                  


today = dt.datetime.now().date()


class Calculator:                                  
                                                 
    def __init__(self, limit):                                         
        self.limit = limit
        self.records = []                                              

    def add_record(self, record):                                      
        self.records.append(record)

    def get_today_stats(self):                                         
        the_cost = 0 
        for record in self.records:                                    
            if record.date == today:                              
                the_cost += record.amount          
        return the_cost       
    
    def get_week_stats(self):
        the_cost = 0 
        one_week_ago = today - dt.timedelta(days=7) 
        for record in self.records:                                   
            if  one_week_ago <= record.date <= today:       
                the_cost += record.amount          
        return the_cost


class Record:                                    
    
    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date == None:                                                
            self.date = today
        else:
            self.date = dt.datetime.strptime(date, "%d.%m.%Y").date()   


class CashCalculator(Calculator): 
    USD_RATE  = 73.18
    EURO_RATE = 81.86
    
    def get_today_cash_remained(self, currency):  
        if currency == "usd":
            currency_rate = self.USD_RATE
            self.name_currency = "USD"
        elif currency == "eur":
            currency_rate = self.EURO_RATE
            self.name_currency = "Euro"
        else:
            currency_rate = 1
            self.name_currency = "руб"

        total_costs_today = self.get_today_stats()
        remains = self.limit - total_costs_today

        if remains > 0:
            return f"На сегодня осталось {round(remains / currency_rate,2)} {self.name_currency}"          
        elif remains == 0:
            return f"Денег нет, держись"
        else: 
            return f"Денег нет, держись: твой долг - {abs(round(remains / currency_rate,2))} {self.name_currency}"

        
class CaloriesCalculator(Calculator):
    
    def get_calories_remained(self):
        total_calories_today = self.get_today_stats()
        remains = self.limit - total_calories_today
        
        if remains >= 0:
            return f"Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {remains} кКал"
        else:
            return f"Хватит есть!"




cash_calculator = CashCalculator(1000)

cash_calculator.add_record(Record(amount=145, comment="кофе")) 

cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))

cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained("eur")