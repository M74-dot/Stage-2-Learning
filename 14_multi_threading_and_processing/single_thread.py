import threading
from threading import Thread
import time


def thread_function():
    print('Started thread function')
    time.sleep(2)
    print('Completed thread function')


thrd = Thread(target = thread_function)
thrd.start()
thrd.join()

print(threading.active_count())
