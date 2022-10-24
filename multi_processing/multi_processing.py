import multiprocessing as mp

def task(a,b):
    print(a+b)
    return a+b

if __name__=='__main__':
    p1 = mp.Process(target= task, args = (1,2))
    p2 = mp.Process(target= task, args = (3,4))
    p1.start()
    p2.start()
    p2.join()
    p1.join()