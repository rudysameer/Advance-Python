import time
import threading

def cal_cube(numbers):
    print("Calculating cube numbers ")
    for num in numbers:
        time.sleep(0.2)
        print(f"cube {num} = {num*num*num}")

    

def cal_square(numbers):
    print("Calculating Square numbers")
    for num in numbers:
        time.sleep(0.2)
        print(f"square {num} = {num*num}")

listy = [1,2,3,4,5,6,7,8,9]
start = time.time()

t1 = threading.Thread(target=cal_square,args=(listy,))
t2 = threading.Thread(target=cal_cube,args=(listy,))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"the total time taken is {time.time()-start} seconds")
