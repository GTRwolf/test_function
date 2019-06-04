import threading
import time
import threadpool
import tensorflow as tf
import queue
import threading




def work():
    print("key is ")
    print ('index %s, curent: ', threading.current_thread())
    time.sleep(1)
    threading.Condition().notify_all()

def sb(x):
    threading.Condition().wait()
    for i in range(100000000000000000000000000000):
        x = x+1
        print(x)
        x = x-1

def gcd(pair):
    a, b = pair
    low = min(a, b)
    for i in range(low, 0, -1):
        if a % i == 0 and b % i == 0:
            return i

numbers = [
    (1963309, 2265973), (1879675, 2493670), (2030677, 3814172),
    (1551645, 2229620), (1988912, 4736670), (2198964, 7876293)
]

def multi_thread(cpu_cores):
    pool = threadpool.ThreadPool(cpu_cores)
    time_for_start = time.time()
    for i in range (5):
        time_work_start = time.time()
        name_list = [233,233]
        requests = threadpool.makeRequests(sb, name_list)
        [pool.putRequest(req) for req in requests]
        pool.wait()
        time_work_end = time.time()
    time_for_end = time.time()
    print("time_work is ", (time_work_end-time_work_start))
    print("time_for is ", (time_for_end - time_for_start))

def thread_queue():

    #开三个线程的线程池
    for i in range(8):
        t = threading.Thread(target=sb)
        t.daemon = True
        t.start()

    for j in range(5):
        q = queue.Queue()
        for j in range(5):
            for i in range(10):
                q.put(None)

def thread_test():
    t1 = threading.Thread(target=sb(500))
    t2 = threading.Thread(target=sb(300))
    t3 = threading.Thread(target=sb(200))
    t4 = threading.Thread(target=sb(600))
    t5 = threading.Thread(target=work())
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()

# def multi_process():
#     pool = ProcessPoolExecutor(max_workers=4)
#     results = list(pool.map(sb, [500,200,300,100]))


thread_test()