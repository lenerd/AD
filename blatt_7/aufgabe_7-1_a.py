import numpy as np
import random


def print_seq(a, l, k):
    if k > 1:
        print_seq(a, l, l[k] - 2)
    print(a[l[k]])


def mnas(a):
    n = len(a)
    m = np.zeros(n)
    l = np.zeros(n, dtype=int)
    m[0] = a[0]
    l[0] = 0
    if a[1] > a[0]:
        m[1] = a[1]
        l[1] = 1
    else:
        m[1] = a[0]
        l[1] = 0
    for i in range(2, n):
        if m[i-2] + a[i] > m[i-1]:
            m[i] = m[i-2] + a[i]
            l[i] = i
        else:
            m[i] = m[i-1]
            l[i] = i - 1
    print(m[n-1])
    print_seq(a, l, n - 1)


def main():
    a = random.sample(range(10), 10)
    print(a)
    mnas(a)


if __name__ == '__main__':
    main()
