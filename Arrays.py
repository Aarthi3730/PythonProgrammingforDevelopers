from array import array

numbers = array("i", [1, 2, 3])
numbers.append(0)      # [1, 2, 3, 0]
numbers.pop(1)         # removes element at index 1 → 2 → [1, 3, 0]

# Remove 2 only if it's still in the array
if 2 in numbers:
    numbers.remove(2)

print(numbers)
