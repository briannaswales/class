def is_leap_year(a_year):
    return a_year % 4 == 0 and (a_year % 100 != 0 or a_year % 400 == 0)


is_leap_year(2021)
