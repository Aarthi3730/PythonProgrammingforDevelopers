import timeit

def code1():
    x = [i for i in range(100)]

def code2():
    x = list(range(100))

print("firstcode:", timeit.timeit(code1, number=10000))
print("secondcode:", timeit.timeit(code2, number=10000))

#print