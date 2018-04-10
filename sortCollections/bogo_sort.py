import random

from typing import List


def bogo_sort(ary: List[float]):
    def is_sorted(ls: List[float]):
        for _p, _next in zip(ls[:-1], ls[1:]):
            if _p > _next:
                return False
        return True

    while not is_sorted(ary):
        random.shuffle(ary)

    return ary


if __name__ == '__main__':
    test_array = [random.randint(0, 10) for i in range(10)]
    print(test_array)
    print(bogo_sort(test_array))
