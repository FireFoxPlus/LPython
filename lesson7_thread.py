from threading import Thread
import time
def my_counter():
    i = 0;
    for i in range(100000):
        i = i + 1
    return True

def main():
    thread_arry ={}
    start_time = time.time()
    for tid in range(2):
        t = Thread(target=my_counter)
        t.start()
        thread_arry[tid] = t
    for i in range(2):
        #本线程执行完成之前，其他线程不能执行
        thread_arry[i].join()
    end_time = time.time()

if __name__ == '__main__':
    main()
