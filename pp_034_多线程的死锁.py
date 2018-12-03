from threading import Thread, Lock, current_thread

numa = 0
numb = 0

locka = Lock()
lockb = Lock()


def do_sth():
    fun1()
    fun2()


def fun1():
    global numa, numb
    locka.acquire()
    try:
        print('%s--fun1()--locka' % current_thread().getName())
        numa += 1
        lockb.acquire()
        try:
            print('%s---fun1()--lockb' % current_thread().getName())
            numb += 1
        finally:
            lockb.release()
    finally:
        locka.release()


def fun2():
    global numa, numb
    lockb.acquire()
    try:
        print('%s--fun2()--lockb' % current_thread().getName())
        numb += 1
        locka.acquire()
        try:
            print('%s---fun2()--locka' % current_thread().getName())
            numa += 1
        finally:
            locka.release()
    finally:
        lockb.release()


tlist = []
for i in range(100):
    t = Thread(target=do_sth)
    tlist.append(t)
    t.start()

for item in tlist:
    item.join()

print('父线程结束')

"""
Thread-1--fun1()--locka
Thread-1---fun1()--lockb
Thread-1--fun2()--lockb
Thread-2--fun1()--locka
"""
