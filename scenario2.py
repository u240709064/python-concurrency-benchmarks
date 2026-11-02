import time
import threading
import multiprocessing

def cpu_task(start, end):
    
    return sum(i * i for i in range(start, end))

def thread_cpu_worker(start, end, result_list, index):
   
    result_list[index] = cpu_task(start, end)

def process_cpu_worker(start, end, result_array, index):
   
    result_array[index] = cpu_task(start, end)

def run_scenario_2(N):
    print(f" SCENARIO 2: CPU-Bound Task (N = {N:,}) ")
    mid = N // 2 

    start_time = time.time()
    thread_results = [0, 0]
    
    t1 = threading.Thread(target=thread_cpu_worker, args=(0, mid, thread_results, 0))
    t2 = threading.Thread(target=thread_cpu_worker, args=(mid, N, thread_results, 1))
    
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    thread_time = time.time() - start_time
    print(f"Thread Time:  {thread_time:.4f} seconds")

    start_time = time.time()
    process_results = multiprocessing.Array('q', 2) 
    
    p1 = multiprocessing.Process(target=process_cpu_worker, args=(0, mid, process_results, 0))
    p2 = multiprocessing.Process(target=process_cpu_worker, args=(mid, N, process_results, 1))
    
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    process_time = time.time() - start_time
    print(f"Process Time: {process_time:.4f} seconds")
    
    if process_time < thread_time:
        print("Winner: MULTIPROCESSING (Cross-over point reached!)\n")
    else:
        print("Winner: THREADING\n")

if __name__ == '__main__':
    workloads = [10000, 100000, 1000000, 10000000, 50000000, 100000000, 200000000]
    for n in workloads:
        run_scenario_2(n)