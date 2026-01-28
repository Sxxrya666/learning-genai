from threading import Thread, current_thread, active_count
import time

def big_task():
    print('starting the big task of counting')
    print('current thread: ', current_thread().name)
    print('active count: ', active_count())
    count = 0
    for _ in range(100_000_00):
        count += 1
    print('ended counting successfully')
    
start = time.perf_counter()

t1 = Thread(target=big_task, name="counter-no-1")
t2 = Thread(target=big_task, name="counter-no-2")


t1.start()
t2.start()
# t1.join()
# t2.join()

finish_time = time.perf_counter() - start
print('finished at: ', finish_time)