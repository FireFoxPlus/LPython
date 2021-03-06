from multiprocessing import Process
import threading
import time
lock = threading.Lock()

def run(info_list,n):
    lock.acquire()
    info_list.append(n)
    lock.release()
    print('%s\n' % info_list)

#线程共享内存，进程不共享内存
if __name__ == '__main__':
     info = []
     for i in range(10):
         p = Process(target=run, args=(info, i))
         p.start()
         p.join()
     time.sleep(1)
     print('threading-----------')
     for i in range(10):
         p = threading.Thread(target=run, args=[info, i])
         p.start()
         p.join()