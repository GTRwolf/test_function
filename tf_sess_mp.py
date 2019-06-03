import tensorflow as tf
import multiprocessing as mp
import time
import threading

class Worker():
    def __init__(self):
        print("Worker_init")


    def sess_test1(self):
        print("sess 1 is running")
        z = tf.Variable(1, name='PID1_Z')
        a = tf.get_variable('var_a', 2)

    def sess_test2(self):
        print("sess 2 is running")
        with tf.name_scope('aaa'):
            c = tf.Variable(3, name='var_c')

    def sess_test3(self):
        print("sess 3 is running")
        with tf.variable_scope('bbb'):
            d = tf.Variable(4, name='var_d')

    def event_test(self,e):
        print("sleep 3 s")
        time.sleep(3)
        e.set()

#主进程中定义global全局变量，无法与子进程共享
global s

a = Worker()
print("s is ",s)
#e = multiprocessing.Event()
#print('the event_set is:',e.is_set())
with mp.Manager() as manager:
    p = mp.Process(target=a.sess_test1,args=())
    q = mp.Process(target=a.sess_test2,args=())
    r = mp.Process(target=a.sess_test3,args=())
    p.start()
    q.start()
    r.start()

    p.join()
    q.join()
    r.join()
    print([str(i.name) for i in tf.global_variables()])
    print([str(i.name) for i in tf.local_variables()])
'''
for j in range(10):
    pool = multiprocessing.Pool(processes=4)
#pool.apply_async(a.act, (d,i))
pool.apply_async(a.sess_test1, (e, 2))
pool.apply_async(a.event_test, (e, ))

pool.close()
pool.join()
'''