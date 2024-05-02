from datetime import datetime
import inflect

p = inflect.engine()
# userbday = input("Enter your birthday (YYYY-MM-DD): ")
userbday = "2023-05-02"
datetime_birthday = datetime.fromisoformat(userbday)
minutes = (datetime.fromisoformat("2024-05-03") - datetime_birthday).days * 24 * 60
print(p.word_to_numbers(minutes, andword=""))
