items=[
    ("Product1",10),
    ("Product2",11),
    ("Product3",12)
]

items.sort(key=lambda item:item[1])
print(items)