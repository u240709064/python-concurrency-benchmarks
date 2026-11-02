# Python Concurrency & GIL Performance Benchmark

An operating systems analysis evaluating performance trade-offs between **Multithreading** and **Multiprocessing** in Python, specifically measuring the impact of the **Global Interpreter Lock (GIL)** and identifying the **Efficiency Crossover Point**[cite: 2].

## 📌 Technical Overview
* **GIL Bottleneck:** Demonstrates how Python's mutex prevents true parallel execution in CPU-bound tasks[cite: 2].
* **Communication Tax:** Measures the ~1 second performance overhead created by process initiation and memory isolation (pickling/serialization)[cite: 3, 5].
* **Break-Even Analysis:** Identifies the exact workload threshold where true process parallelism outweighs process creation overhead[cite: 2].

## 💻 Benchmark Environment
* **CPU:** Intel Core i7 13th Gen (14 Cores)[cite: 4, 5]
* **RAM:** 16 GB[cite: 4, 5]
* **OS:** Windows 11 Pro[cite: 5]
* **Runtime:** Python 3.x

## 📊 Benchmark Results

### Scenario 1: I/O-Bound Task (50 Tasks)
Threading is superior for I/O tasks as GIL is released during wait times (`time.sleep`) without heavy process creation costs[cite: 4, 5].

| Execution Model | Time (seconds) | Winner |
|---|---|---|
| Sequential | 5.0218s | -[cite: 4] |
| **Multi-threading (5 Threads)** | **1.0078s** | **Winner 🏆**[cite: 4] |
| Multi-processing (5 Processes) | 1.9039s | High process tax[cite: 4] |

### Scenario 2: CPU-Bound Task & Efficiency Crossover
Finding the break-even point by increasing workload size ($N$)[cite: 4]:

| Workload ($N$) | Thread Time (s) | Process Time (s) | Winner |
|---|---|---|---|
| 10,000 | 0.0016s | 1.0235s | Threading[cite: 4] |
| 1,000,000 | 0.0441s | 1.0246s | Threading[cite: 4] |
| 50,000,000 | 2.0370s | 2.1746s | Threading[cite: 4] |
| **100,000,000** | **4.0176s** | **3.2150s** | **Multiprocessing 🏆**[cite: 4] |
| 200,000,000 | 8.5431s | 6.0731s | **Multiprocessing 🏆**[cite: 4] |

> **Key Finding:** The efficiency crossover point lies between $N = 50,000,000$ and $N = 100,000,000$[cite: 5]. Beyond this workload, process parallelism compensates for the initial process startup overhead[cite: 5].

## 📁 Repository Structure
* `scenario1.py`: I/O-bound execution comparison script[cite: 8].
* `scenario2.py`: CPU-bound break-even benchmark script[cite: 9].
* `Performance_Report.pdf`: Comprehensive technical report detailing memory models and GIL mechanics[cite: 2].

## 🚀 How to Run
```bash
# Run I/O simulation
python scenario1.py

# Run CPU break-even simulation
python scenario2.py
