# Create a decorator function to check that the argument passed to the function factorial is a non-negative integer:
# Create a factorial function which finds the factorial of a number.
# Use the decorator to decorate the factorial function to only allow factorial of non-negative integers.

def my_decorator(func):
    def wrapper(x,*args, **kwargs):
        print("Inside the decorator")
        if not isinstance(x,int) or x<0:
            raise ValueError("input must be non negative integer")
        result = func(x,*args,**kwargs)
        return result
    return wrapper

@my_decorator
def factorial(x):
    if x ==0:
        return 1
    if x>=1:
        result = 1
        for i in range(1,x+1):
            result *=i
        return result
        

print(factorial(3))
print(factorial(0))
for i in range(1,10):
    print(factorial(i))

try:
    print(factorial(-5))
except ValueError as e:
    print(e)    
