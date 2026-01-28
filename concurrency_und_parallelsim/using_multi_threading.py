from threading import Thread
import time

def perform_heavy_task(arg1, arg2, arg3):
    start_time = time.perf_counter()
    print(f'status: {arg1} 40%')
    time.sleep(2)
    print(f'status: {arg2} 80%')
    time.sleep(2)
    print(f'status: {arg3} 100%')
    print(time.perf_counter() - start_time)


def main():
    func1_thread = Thread(target=perform_heavy_task, args=('eat', 'beat', 'bleet'))
    func1_thread.start()
    func2_thread = Thread(target=perform_heavy_task, args=('lick', 'suck', 'cuck'))
    func2_thread.start()
    func1_thread.join()
    func2_thread.join()
print(main())
    
