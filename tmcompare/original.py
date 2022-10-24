import random
import time

start_time = time.time()
for i in range(10000000):
    a = random.randint(0,1000)
print(time.time()- start_time)
    