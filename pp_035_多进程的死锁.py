from multiprocessing import Process, Lock, current_process, Value

numa = Value('i', 0)
numb = Value('i', 0)

locka = Lock()
lockb = Lock()


def do_sth(numa, numb):
    fun1(numa, numb)
    fun2(numa, numb)


def fun1(numa, numb):
    locka.acquire()
    try:
        print('%s--fun1()--locka' % current_process().pid)
        numa.value += 1
        lockb.acquire()
        try:
            print('%s---fun1()--lockb' % current_process().pid)
            numb.value += 1
        finally:
            lockb.release()
    finally:
        locka.release()


def fun2(numa, numb):
    lockb.acquire()
    try:
        print('%s--fun2()--lockb' % current_process().pid)
        numb.value += 1
        locka.acquire()
        try:
            print('%s---fun2()--locka' % current_process().pid)
            numa.value += 1
        finally:
            locka.release()
    finally:
        lockb.release()

if __name__ == '__main__':

    plist = []
    for i in range(100):
        p = Process(target=do_sth, args=(numa, numb))
        plist.append(p)
        p.start()

    for item in plist:
        item.join()

    print('父进程结束')
