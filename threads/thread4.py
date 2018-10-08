import threading
import time

class MyThread(threading.Thread):
    def __init__(self, func, name=""):
        threading.Thread.__init__(self)
        self.name = name
        self.func = func

    def run(self):
        while 1:
            self.func()

def myfunction():
    print("myfunction")
    time.sleep(2)

if __name__=="__main__":
    t1 = MyThread(myfunction,  "thread1")
    t2 = MyThread(myfunction,  "thread2")
    t1.start()
    t2.start()
    while 1:
        time.sleep(5)
        print("bwahhh")
    t1.join()
    t2.join()
