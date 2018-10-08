import multiprocessing 
import time

def counter1(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value += 1
        lock.release()

def counter2(number,lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()
        number.value -= 1
        lock.release()


if __name__=="__main__":
    number = multiprocessing.Value('i', 100)
    lock = multiprocessing.Lock()
    t1 = multiprocessing.Process(target=counter1, args=(number,lock))
    t2 = multiprocessing.Process(target=counter2, args=(number,lock))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("number: ", number.value)
