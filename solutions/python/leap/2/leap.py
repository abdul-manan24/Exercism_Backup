def leap_year(year):
    is_leap = bool()
    if year % 100 == 0:
        is_leap = year % 400 == 0
        return is_leap
    is_leap = year % 4 == 0
    return is_leap
    
