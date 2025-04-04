items = [
    ("Product1", 10),
    ("Product2", 11),
    ("Product3", 12)
]

prices = [item[1] for item in items]
filtered = [item for item in items if item[1] >= 10]

print(prices)
print(filtered)
