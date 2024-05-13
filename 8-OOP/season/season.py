from datetime import datetime
from datetime import date

import inflect

p = inflect.engine()
userbday = input("Enter your birthday (YYYY-MM-DD): ")
datetime_birthday = datetime.fromisoformat(userbday)
delta_days = (
    datetime.combine(date.today(), datetime.min.time()) - datetime_birthday
).days
minutes = delta_days * 24 * 60
print(minutes)
print(p.number_to_words(minutes, andword="").capitalize(), "minutes.")
