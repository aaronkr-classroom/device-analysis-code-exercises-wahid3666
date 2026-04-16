# SayDays.py (202310012_Wahid)

class SayDays:
    def __init__(self, year: int, month: int, day: int):
        self.year   = year
        self.month  = month
        self.day    = day
        
    def is_leap(self) -> bool:
        y = self.year
        # Leap year? February = 29 : not = 28
        # Leap year? Year = 366 : not 365
        # Using in 2 places -> let's return bool
        return(
            (y% 4 == 0 and y % 100 != 0) or
            (y% 400 == 0)
        )
    
    def days(self) -> int:
        # From Jan 1, how many days until now?
        days_in_month = [
            31, 29 if self.is_leap() else 28, 31, 30,
            31, 30, 31, 31,
            30, 31, 30, 31
            ] # 31 + 28 = 59 + 31 = 90 + 16 = 116
        
        total = 0
        m = 0 # 0th month = January
        
        # Calculates all days in all previous months
        while m < self.month - 1: # 0 < 4
            total += days_in_month[m]
            m += 1
            
        # Add the days in this month until today (given date)
        total += self.day # property not function return
        return total
    
    def days_left(self) -> int:
        # Until Dec 31, how many days left? 366? 365?
        total_days = 366 if self.is_leap() else 365
        return total_days - self.days() # not 16th , but 116
        
    def weekday(self) -> int:
        # Use Zeller's formula to find the numeric day of the week
        y = self.year
        m = self.month
        d = self.day
        
        if  m <3: # January? February?
            m += 12
            y -= 1
         
        K = y % 100   # Last two digits of the year  (2026 % 100 = 26)
        J = y // 100  # First two digits of the year (1926 // 100 = 19)
        
        h = (d + ( 13 * ( m + 1)) //
             5 + K + K // 4 + J // 4 + 5 * J ) % 7
        
        return h # 5 = Thursday
        
    def weekday_name(self) -> str:
        # print the English name of the numeric day of the week
        names = [
            "Saturday", "Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday"
            ]
        return names[self.weekday()] # 5 -> "Thrusday"
    
# RUN IT!!
while True:
    year  = int(input("What year is it?  "))
    month = int(input("What month is it? "))
    day   = int(input("What day is it?   "))
    
    date  = SayDays(year, month, day)
    
    
    print("Days after Jan 1:  ", date.days())
    print("Days until Dec 31: ", date.days_left())
    print("Numeric day of the week: ", date.weekday())
    print("English day of the week: ", date.weekday_name())
        
        
        
        
        
        
        