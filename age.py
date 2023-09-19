
from datetime import datetime

user_birthday = input("please enter birthday in format 01-01-1999: ")


def age_calc(user_birthday):
   user_birthday_format = datetime.strptime(user_birthday, "%d-%m-%Y")
   today_date = datetime.today()
   age = today_date.year - user_birthday_format.year - ((today_date.month, today_date.day) < (user_birthday_format.month,user_birthday_format.day))
   return age

print(age_calc(user_birthday))


