from multiprocessing import Process,Manager

def func(i, d):
    d[i] = i + 100
    print(d.values())

if __name__ == '__main__':
    m = Manager()
    d = m.dict()

    for i in range(5):
        # 让子进程去修改主进程的特殊字典
        p = Process(target=func, args=(i, d))
        p.start()
    p.join()