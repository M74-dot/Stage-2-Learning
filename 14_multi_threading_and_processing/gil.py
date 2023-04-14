import threading
from threading import Thread


kill_threads = False

def working_thread():
    while True:
        if kill_threads == True:
            return


# thrd = Thread(target = working_thread)
# thrd.start()
# print(threading.active_count())

thrd1 = Thread(target = working_thread)
thrd2 = Thread(target = working_thread)

thrd1.start()
print(threading.active_count())
thrd2.start()
print(threading.active_count())

# stop both the threads
kill_threads = True
print(threading.active_count())
