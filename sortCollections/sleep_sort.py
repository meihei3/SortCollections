import random
import threading
import time
from typing import List


def sleep_sort(ary: List[float]):
    def f(n: float, q: List[float]):
        time.sleep(n)
        q.append(n)

    queue = []
    threads = [threading.Thread(target=f, args=(i, queue)) for i in ary]
    for th_me in threads:
        th_me.start()
    for th_me in threads:
        th_me.join()

    return queue


if __name__ == '__main__':
    test_array = [random.randint(0, 10) for i in range(10)]
    print(test_array)
    print(sleep_sort(test_array))
