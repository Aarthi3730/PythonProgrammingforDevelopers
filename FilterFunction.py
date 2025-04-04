items=[
    ("Product1",10),
    ("Product2",11),
    ("Product3",12)
]
filtered=list(filter(lambda item:item[1]>=10,items))
print(filtered)