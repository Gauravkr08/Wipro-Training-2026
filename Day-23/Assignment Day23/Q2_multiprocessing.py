import math
import time
import multiprocessing

numbers = [50000, 60000, 55000, 45000, 70000]

def calculate_factorial(n):
    return math.factorial(n)

def sequential_execution():
    start_time = time.time()

    results = []
    for num in numbers:
        result = calculate_factorial(num)
        results.append(result)

    end_time = time.time()

    print("\nSequential Results:")
    for num, res in zip(numbers, results):
        print(f"Factorial of {num} calculated.")

    print("Sequential Time:", end_time - start_time, "seconds")

def multiprocessing_execution():
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(calculate_factorial, numbers)

    end_time = time.time()

    print("\nMultiprocessing Results:")
    for num, res in zip(numbers, results):
        print(f"Factorial of {num} calculated.")

    print("Multiprocessing Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    print("Starting Sequential Execution...")
    sequential_execution()

    print("\nStarting Multiprocessing Execution...")
    multiprocessing_execution()
