def calculated_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less")
    return 10 / age

try:
    calculated_xfactor(-1)
except ValueError as error:
    print(error)
