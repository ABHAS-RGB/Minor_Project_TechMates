import requests
import threading
import time
import psutil

URL = "http://127.0.0.1:5000/cpu-load"


def send_request():
    try:
        requests.get(URL)
    except:
        pass


print("\nStarting Load Test...\n")

for round in range(1, 20):

    threads = []

    # simulate 20 concurrent users
    for _ in range(20):
        t = threading.Thread(target=send_request)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent

    print(f"Round {round:02d} | CPU Usage: {cpu}% | Memory Usage: {memory}%")

print("\nLoad test finished.\n")