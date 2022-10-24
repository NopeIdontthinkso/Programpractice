import random
import time
import threading

def njad():
    for i in range(2500000):
        a = random.randint(0,1000)

start_time = time.time()
t1 = threading.Thread(target=njad)
t2 = threading.Thread(target=njad)
t3 = threading.Thread(target=njad)
t4 = threading.Thread(target=njad)
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
print(time.time() - start_time)