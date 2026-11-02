import time
import threading
import multiprocessing

def io_sequential():
    
    for _ in range(50):
        time.sleep(0.1)

def io_thread_worker(tasks, lock, counter):
    
    for _ in range(tasks):
        time.sleep(0.1)
        with lock:
            counter[0] += 1

def io_process_worker(tasks, lock, counter):
    
    for _ in range(tasks):
        time.sleep(0.1)
        with lock:
            counter.value += 1

if __name__ == '__main__':
    print("SCENARIO 1: I/O Simulation (50 Tasks)")
    
    
    start_time = time.time()
    io_sequential()
    print(f"Sequential Time: {time.time() - start_time:.4f} seconds")

    
    start_time = time.time()
    thread_lock = threading.Lock()
    thread_counter = [0]
    threads = []
    
    for _ in range(5):
        t = threading.Thread(target=io_thread_worker, args=(10, thread_lock, thread_counter))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Multi-threading Time (5 Threads): {time.time() - start_time:.4f} seconds | Completed Tasks: {thread_counter[0]}")

    
    start_time = time.time()
    process_lock = multiprocessing.Lock()
    process_counter = multiprocessing.Value('i', 0)
    processes = []
    
    for _ in range(5):
        p = multiprocessing.Process(target=io_process_worker, args=(10, process_lock, process_counter))
        processes.append(p)
        p.start()
        
    for p in processes:
        p.join()
        
    print(f"Multi-processing Time (5 Processes): {time.time() - start_time:.4f} seconds | Completed Tasks: {process_counter.value}")