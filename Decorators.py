import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result  = func(*args,**kwargs)
        end = time.time()
        elapsed_time = (end-start)*1000
        print(f"{func.__name__} took {elapsed_time} miliseconds")
        return result
    return wrapper

@time_it
def square(numbers):
    result = []
    for num in numbers:
        result.append(num*num)
    return result

@time_it
def cube(numbers):
    result = []
    for num in numbers:
        result.append(num*num*num)
    end = time.time()
    return result   

array = range(1,100000)
square(array)
cube(array)

