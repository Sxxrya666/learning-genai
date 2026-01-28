from multiprocessing import Process 
import os
import time


def perform_heavy_task(arg1, arg2): 
    print('total cores engaged: ', os.cpu_count())
    print('process id: ', os.getpid())
    start_time = time.perf_counter()
    print(f"STARTED TASK FOR ARGS: {arg1}, {arg2}")
    print(f'status: {arg1} 20%')
    time.sleep(2)
    print(f'status: {arg2} 40%')
    time.sleep(2)
    print(f'status: {arg1} 60%')
    time.sleep(2)
    print(f'status: {arg2} 80%')
    time.sleep(2)
    print(f'100% DONE FOR {arg1}, {arg2} !')
    print(f"time taken to finish {os.getpid()}: ", time.perf_counter() - start_time)


if __name__ == "__main__": #! very very important line!!! it will stop from creating infinite nested child processes
    list_of_parallel_processes = [
        Process(target=perform_heavy_task, args=('a', 'b'))
        for _ in range(6) 
    ]

# start them process
    for pll_process in list_of_parallel_processes:
        pll_process.start()

        
        
    for pll_process in list_of_parallel_processes:
        pll_process.join()
        
        