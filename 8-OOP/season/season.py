from datetime import datetime
import inflect

p = inflect.engine()
# userbday = input("Enter your birthday (YYYY-MM-DD): ")
userbday = "2021-05-09"
datetime_birthday = datetime.fromisoformat(userbday)
delta_days = (datetime.fromisoformat("2023-05-09") - datetime_birthday).days
minutes = delta_days * 24 * 60
print(minutes)
print(p.number_to_words(minutes, andword="").capitalize(), "minutes.")
