import threading
#from multiprocessing import Queue
import queue
import random
import time
import sys
import signal

def signal_handler(sig, frame):
    print("cntrl-c pressed. Exiting....")
    sys.exit(0)

data_q = queue.Queue()

class Producer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            integer = random.randint(0,255)
            self.queue.put(integer)
            print("Prod: %d put into queue"%integer)
            time.sleep(3)

class Consumer(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            integer =self.queue.get()
            print("Cons: %d popped from queue"%integer)
            self.queue.task_done() #indicate to queue that item was retrieved
            time.sleep(1)

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    p = Producer(data_q)
    c = Consumer(data_q)
    p.setDaemon(True)
    c.setDaemon(True)
    p.start()
    c.start()
    while True:
        pass


