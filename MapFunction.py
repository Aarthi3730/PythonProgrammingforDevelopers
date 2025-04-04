items=[
    ("Product1",10),
    ("Product2",11),
    ("Product3",12)
]
prices=list(map(lambda item:item[1],items))
for item in prices:
    print(item)