def multiply(*list):
    total=1
    for number in list:
        total*=number
    return total
print(multiply(5,4,6,7))
