import threading
from threading import Thread
import time


class MyThread(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        print('Thread is running ')
        time.sleep(2)
        print('Exiting thread ')


print(threading.active_count())
mt = MyThread()
mt.start()  # run method will call
print(threading.active_count())
