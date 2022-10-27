import threading
var = 0
lock = threading.Lock()
def task1():
    global var
    global lock
    with lock:
        a = 0
        print('11:', var)
        for i in range(30000):
            a += 1
        var += 1
        print('12:', var)

def task2():
    global var
    global lock
    with lock:
        a = 0
        print('21:', var)
        for i in range(200000):
            a += 1
        var += 2
        print('22:', var)

if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()