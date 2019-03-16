# Созадть очередь из задач. Создать воркеров которые будут делать выборки из очереди и  выполнять эти задачи.
# Количество воркеров - опциональный аргумент. Количество задач - опциональный аргумент.  1 воркер == 1 тред
import threading
from queue import Queue
import time
import requests


def get_request(url):
    req = requests.get(url)
    print('Request {} completed'.format(req))


class ThreadQueue(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            url = self.queue.get()
            try:
                get_request(url)
            finally:
                self.queue.task_done()


def main():
    start = time.time()
    urls = ['https://httpbin.org/get'] * 5
    queue = Queue()
    for w in range(5):
        worker = ThreadQueue(queue)
        worker.daemon = True
        worker.start()
    for url in urls:
        queue.put(url)
    queue.join()
    print('Completed in {} seconds'.format(time.time() - start))


main()

