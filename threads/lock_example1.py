import multiprocessing 
import time

def counter1(number):
    for i in range(100):
        time.sleep(0.01)
        number.value += 1

def counter2(number):
    for i in range(100):
        time.sleep(0.01)
        number.value -= 1


if __name__=="__main__":
    number = multiprocessing.Value('i', 100)
    t1 = multiprocessing.Process(target=counter1, args=(number,))
    t2 = multiprocessing.Process(target=counter2, args=(number,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("number: ", number.value)
