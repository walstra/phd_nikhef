# multi_threaded.py
import time
from threading import Thread

COUNT = 50000000

def countdown(n):
    while n>0:
        n -= 1

t1 = Thread(target=countdown, args=(COUNT//2,))
t1.setName("thread1")
t1.setDaemon(True)
print("Thread1 is alive: ", t1.isAlive())

start = time.time()
t1.start()
print("Thread1 is alive: ", t1.isAlive())
#t1.join() #if comment: don't wait until the thread exits
end = time.time()

print('Time taken in seconds -', end - start)
print(t1.isAlive())
