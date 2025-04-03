numbers=[3,5,29,13,8,11]
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)

items=[
    ("Product1",10),
    ("Product2",11),
    ("Product3",12)
]
def sort_item(items):
    return items[1]
items.sort(key=sort_item)
print(items)