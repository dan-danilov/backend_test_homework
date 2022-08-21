import datetime as dt


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:
    def __init__(self, limit) -> None:
        self.limit = limit
        self.today = dt.date.today()
        self.records = []

    def add_record(self, new_record):
        self.records.append(new_record)

    def get_today_stats(self):
        today_sum = 0
        for record in self.records:
            if record.date == self.today:
                print(record.date)
                today_sum += record.amount
        return today_sum

    def get_week_stats(self):
        week_stats = 0
        week_ago = self.today - dt.timedelta(7)
        for record in self.records:
            if week_ago <= record.date:
                week_stats = + record.amount
        return week_stats


class CashCalculator(Calculator):
    USD_RATE = 70.0
    EURO_RATE = 77.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency='rub'):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.limit - self.get_today_stats()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            message = (f'Денег нет, держись: твой долг - {cash_remained} '
                       f'{name}')
        return message


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        calories_remained = self.limit - self.get_today_stats()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


def main():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment="кофе"))
    cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cash_calculator.add_record(
        Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    print(cash_calculator.get_today_cash_remained("rub"))
    cal_calculator = CaloriesCalculator(1000)
    cal_calculator.add_record(Record(amount=145, comment="кофе"))
    cal_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
    cal_calculator.add_record(
        Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
    print(cal_calculator.get_calories_remained())


if __name__ == '__main__':
    main()
