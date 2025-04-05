try:
    file = open("data.txt", "r")
    age = int(input("Age: "))
except ValueError:
    print("You didn't enter a valid age.")
except FileNotFoundError:
    print("File not found.")
finally:
    # Only try to close if file was successfully opened
    try:
        file.close()
    except NameError:
        pass
