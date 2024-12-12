#     Create Generator method such that every time it will returns a next square number

# for exmaple : 1 4 9 16 ..
def square():
    a=1
    while True:
        yield a*a
        a = a+1

for sq in square():
    if sq>100:
        break
    print(sq)


     