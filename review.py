# !/usr/bin/python3
# coding=utf-8
# ********************************************************
#   > OS     : OS X 10.11.3
#   > Author : JasonGUTU
#   > Mail   : hellojasongu@gmail.com
#   > Time   : 2016/4/27
# ********************************************************
import pickle
import threading
import queue

import requests


def request_review(url_package, status_code):
    url = url_package[2]
    if not url.startswith('http://'):
        if status_code == 403:
            url = 'https://' + url
        else:
            url = 'http://' + url
    try:
        request = requests.get(url)
        status = request.status_code
        print(' get status:%s, url:%s' % (status, url_package[2]))
        request.close()
    except:
        status = 0
    return status


class Review(threading.Thread):

    def run(self):
        while True:
            if error_queue.qsize() != 0:
                try:
                    url_package = error_queue.get()
                    print('select url:', end='')
                except:
                    continue
                index, package = url_package
                print('%s,' % index)
                package[1] = request_review(package, package[1])
                url_package_list[index] = package
            else:
                break


def load_queue(url_package_list):
    for i, package in enumerate(url_package_list):
        if package[1] == 0 or package[1] == 403:
            error_package = [i, package[:]]
            error_queue.put(error_package)
            print('put into queue %s' % i)


if __name__ == '__main__':
    url_package_list = pickle.load(open('re.plk', 'rb'))
    print('opened')
    error_queue = queue.Queue()
    print('start queue')
    load_queue(url_package_list)
    threads_number = 10
    threads_pool = list()
    print('start thread')
    for i in range(threads_number):
        print('thread %s started' % i)
        t = Review()
        threads_pool.append(t)
    for thread in threads_pool:
        thread.start()
    for thread in threads_pool:
        thread.join()
    result_list = open('result.plk', 'wb')
    pickle.dump(url_package_list, result_list)
