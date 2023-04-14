import multiprocessing as mp
from multiprocessing import Process


def working_process():
    while True:
        pass


proc1 = Process(target = working_process)
proc2 = Process(target = working_process)

proc1.start()
proc2.start()


proc1.terminate()
proc1.close()

proc2.terminate()
proc2.close()
