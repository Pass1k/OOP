class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return f"День: {self.day}    Месяц: {self.month}    Год: {self.year}"

    @classmethod
    def from_string(cls, date_string):
        day, month, year = map(int, date_string.split('-'))
        if cls.is_date_valid(day, month, year):
            return cls(day, month, year)
        else:
            raise ValueError('Некорректная дата')

    @classmethod
    def is_date_valid(cls, day, month, year):
        if 1 <= month <= 12:
            if month in {1, 3, 5, 7, 8, 10, 12}:
                days_in_month = 31
            elif month == 2:
                if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
                    days_in_month = 29
                else:
                    days_in_month = 28
            else:
                days_in_month = 30
            return 1 <= day <= days_in_month
        else:
            return False


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid(10, 12, 2077))
print(Date.is_date_valid(40, 12, 2077))

