class Date:

    def __init__(self, day = "", month = "", year = ""):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        return "day = {}, month = {}, year = {}".format(self.day, self.month, self.year)

    def add_date(self, add_day):

        cal_day = self.day + add_day

        if self.month == 1 or self.month == 3 or self.month == 5 or self.month == 7 or self.month == 8 or self.month == 10 or self.month == 12:

            if cal_day > 31 and self.month == 12:
                self.month = 1
                cal_day -= 31
                self.year += 1
                return print("{}day add. {}.{}.{}".format(add_day, cal_day, self.month, self.year))

            elif cal_day > 31:
                cal_day -= 31
                self.month += 1
                return print("{}day add. {}.{}.{}".format(add_day, cal_day, self.month, self.year))

            else:
                return print("{}day add. {}.{}.{}".format(add_day, cal_day, self.month, self.year))

        elif self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            if cal_day >30:
                cal_day -= 30
                self.month += 1
            else:
                return print("{}day add. {}.{}.{}".format(add_day, cal_day, self.month, self.year))

        elif self.month == 2:
            if cal_day >28:
                cal_day -= 28
                self.month += 1
                return print("{}day add. {}.{}.{}".format(add_day, cal_day, self.month, self.year))
