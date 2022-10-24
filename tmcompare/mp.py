import random
import time
import multiprocessing as mp

def njad():
    for i in range(2500000):
        a = random.randint(0,1000)

if __name__ == '__main__':
    start_time = time.time()
    t1 = mp.Process(target=njad)
    t2 = mp.Process(target=njad)
    t3 = mp.Process(target=njad)
    t4 = mp.Process(target=njad)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print(time.time() - start_time)