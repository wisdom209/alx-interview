#!/usr/bin/python3
"""N queens algorithm"""
import sys

""""
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]
julien@ubuntu:~/0x08. N Queens$ ./0-nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
julien@ubuntu:~/0x08. N Queens$ 
"""


def n_queens():
    """N queens function"""
    arguments = sys.argv

    if (len(arguments) == 1):
        print('Usage: nqueens N')
        sys.exit(1)

    n = arguments[1]
    counter = 1

    try:
        n = int(n)
        if (type(n) is not int):
            print('N must be a number')
            sys.exit(1)
    except Exception:
        print("N must be a number")
        sys.exit(1)

    if (n < 4):
        print("N must be at least 4")
        sys.exit(1)

    for i in range(n-2):

        outer_list = []
        prev = i + 1
        for x in range(n):
            inner_list = []
            if x == 0:
                inner_list.append(x)
                inner_list.append(i + 1)
            else:
                add_num = i + 2
                inner_list.append(x + 1)
                inner_list.append((prev + add_num) % (n + 1))
                prev = (prev + add_num) % (n + 1)
                print(i, prev)
            outer_list.append(inner_list)
        print(outer_list)


if __name__ == '__main__':
    n_queens()
