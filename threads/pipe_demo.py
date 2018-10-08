from multiprocessing import Process, Pipe
def worker(conn):
    while True:
        item = conn.recv()
        if item == "end":
            break
        print(item)

def master(conn):
    conn.send("hello")
    conn.send("world")
    conn.send("end")

if __name__ == "__main__":
    a, b = Pipe()
    w = Process (target = worker, args = (a,))
    m = Process (target = master, args = (b, ))
    w.start()
    m.start()
    w.join()
    m.join()
    
