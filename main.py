# Leap-Year-Indicator
print("Verify if a year is leap or not")

year = int(input("Which year do you want to check? "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(f"The year {year} is a Leap year")
    else:
      print (f"The year {year} is not a leap year")
  else:
    print(f"The year {year} is a Leap year")
else:
  print (f"The year {year} is not a leap year")