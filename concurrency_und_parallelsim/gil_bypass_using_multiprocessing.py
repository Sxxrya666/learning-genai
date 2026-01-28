from multiprocessing import Process, active_children, cpu_count 
import time

def big_task():
    print('starting the big task of counting')
    print(f"""
Active children: {active_children()}
CPU count during program run: {cpu_count()} cores
          """)
    count = 0
    for _ in range(100_000_000):
        count += 1
    print('ended counting successfully')
    
    
start = time.perf_counter()

if __name__ == "__main__":
    p1 = Process(target=big_task, name='big-task-1')
    p2 = Process(target=big_task, name='big-task-2')


    p1.start()
    p2.start()

    p1.join()
    p2.join()

    finish_time = time.perf_counter() - start
    print('finished at: ', finish_time)