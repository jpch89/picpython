from multiprocessing import RLock, Process, Value

numa = Value('i', 0)
numb = Value('i', 0)

rlock = RLock()


def do_sth(numa, numb):
    rlock.acquire()
    try:
        adda(numa)
        addb(numb)
    finally:
        rlock.release()


def adda(numa):
    rlock.acquire()
    try:
        numa.value += 1
    finally:
        rlock.release()


def addb(numb):
    with rlock:
        numb.value += 1

if __name__ == '__main__':
    plist = []
    for i in range(10):
        p = Process(target=do_sth, args=(numa, numb))
        plist.append(p)
        p.start()

    for item in plist:
        item.join()

    print(numa.value)
    print(numb.value)

"""
10
10
"""

"""
小结

RLock 也遵守上下文管理协议，所以可以使用 with 语句。
"""