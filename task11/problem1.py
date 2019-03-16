# Написать функцию которая будет выполнять запросы на https://httpbin.org/ с использованием нескольких потоков
import requests
import threading
import time

urls = ['https://httpbin.org/get'] * 5
start = time.time()


def get_request(url):
    req = requests.get(url)
    print('Request {} completed in {} seconds'.format(req, time.time() - start))


def use_threads():
    threads = [threading.Thread(target=get_request, args=(url, )) for url in urls]
    for thread in threads:
        thread.start()
        thread.join()
    return 'Threading completed in {} seconds'.format(time.time() - start)


use_threads()

