from datetime import datetime

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

millenium = datetime(1999, 12,31)
dob = datetime(year, month, day)

if dob < millenium:
    print(f"You were {(millenium - dob).days} days old on the eve of the new millennium.")
else:
    print("You weren't born yet on the eve of the new millennium.")
