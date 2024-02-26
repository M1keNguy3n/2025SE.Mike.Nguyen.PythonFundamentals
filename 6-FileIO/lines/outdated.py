str = input("Enter a valid date: ")
dict = {
    "January": "01",
    "February": "02",
    "March": "03",
    "April": "04",
    "May": "05",
    "June": "06",
    "July": "07",
    "August": "08",
    "September": "09",
    "October": "10",
    "November": "11",
    "December": "12",
}


prompt = True
date = ""
while prompt:
    if not str[0:2].isnumeric():
        iso_date = str.replace(",", "")
        try:
            month, day, year = iso_date.split(" ")
        except ValueError:
            str = input("Enter a valid date: ")
            continue
    else:
        try:
            month, day, year = str.split("/")
        except ValueError:
            str = input("Enter a valid date: ")
            continue
    # Day check: 0 < day < 32
    if int(day) > 0 and int(day) < 32:
        date += day
        date += "-"
    else:
        date = ""
        str = input("Enter a valid date: ")
        continue
    # Month check:
    #   Non-Numeric: Check dict, if not, fails
    #   Numeric: Check 0 < month < 13
    if not month.isnumeric():
        if month in dict:
            date += dict[month]
            date += "-"
        else:
            date = ""
            str = input("Enter a valid date: ")
            continue
    elif int(month) < 13 and int(month) > 0:
        date += month
        date += "-"
    else:
        date = ""
        str = input("Enter a valid date: ")
        continue
    # Year check: year > 0
    if int(year) > 0:
        date += year
        break
    else:
        str = input("Enter a valid date: ")
        continue
print(date)
