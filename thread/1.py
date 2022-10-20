import threading
import time

def main(num):
    print('Start', num)
    time.sleep(2)
    print('End', num)

thread_list = []
t1 = threading.Thread(target=main, args=(1,))
t2 = threading.Thread(target=main, args=(2,))
t3 = threading.Thread(target=main, args=(3,))
thread_list += [t1, t2, t3]

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()

#./
