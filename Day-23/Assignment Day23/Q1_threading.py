import requests
import threading
import time

urls = [
    "https://example.com/data1",
    "https://example.com/data2",
    "https://example.com/data3",
    "https://example.com/data4"
]

def download_file(url, filename):
    try:
        response = requests.get(url)
        with open(filename, "w", encoding="utf-8") as file:
            file.write(response.text)
        print(f"{filename} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

def sequential_download():
    start_time = time.time()

    for i, url in enumerate(urls):
        filename = f"data{i+1}.txt"
        download_file(url, filename)

    end_time = time.time()
    print("\nSequential Download Time:", end_time - start_time, "seconds")

def threaded_download():
    start_time = time.time()

    threads = []

    for i, url in enumerate(urls):
        filename = f"data{i+1}.txt"
        thread = threading.Thread(target=download_file, args=(url, filename))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print("\nThreaded Download Time:", end_time - start_time, "seconds")


if __name__ == "__main__":
    print("Starting Sequential Download...\n")
    sequential_download()

    print("\nStarting Threaded Download...\n")
    threaded_download()
