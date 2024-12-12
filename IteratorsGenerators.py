my_list = [1,2,3,4,5,6,"this","Baby"]
iter = iter(my_list)
rev = reversed(my_list)
print(next(iter))
print(next(iter))
print(next(iter))


print("Breaking the Line Reversing \n")
print(next(rev))
print(next(rev))
print(next(rev))
print(next(rev))

def generator():
    yield "sameer"
    yield "loves"
    yield "Technology"
    
gen  =generator()


print(next(gen))
print(next(gen))
print(next(gen))