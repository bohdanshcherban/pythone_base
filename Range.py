for i in range(5, 101, 5):
    print(i, end=", ")

i = (range(5, 101, 5))
print("first:", i[0], "second:", i[-1])

i = sum(range(5, 101, 5))
print("sum = ", i)
