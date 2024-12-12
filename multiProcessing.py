import multiprocessing.process
import time
import multiprocessing


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

if __name__ == "__main__":
    listy = [1,2,3,4,5,6,7,8,9]
    start = time.time()

    p1 = multiprocessing.Process(target=cal_square,args=(listy,))
    p2 = multiprocessing.Process(target=cal_cube,args=(listy,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print(f"the total time taken is {time.time()-start} seconds")
