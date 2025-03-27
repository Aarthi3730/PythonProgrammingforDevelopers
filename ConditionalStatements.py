age = int(input())
if age >= 18:
    if age >= 21:
        print("You can drink alcohol.")
    else:
        print("You can vote but cannot drink alcohol.")
else:
    print("You are a minor.")