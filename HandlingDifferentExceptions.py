try:
    age=int(input("Age: "))
    xfactor=10/age
except(ValueError,ZeroDivisionError):
    print("You didn't enter a valid age")
else:
    print("N exceptions were throw")