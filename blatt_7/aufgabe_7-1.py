import numpy as np


def max_non_adjacent_sum(a):
    tab = np.zeros((len(a), 2))
    tab[0] = a[0], 0
    if a[1] > a[0]:
        tab[1] = a[1], 1
    else:
        tab[1] = a[0], 0
    for i in range(2, len(a)):
        if tab[i-2, 0] + a[i] > tab[i-1, 0]:
            tab[i] = tab[i-2, 0] + a[i], i
        else:
            tab[i] = tab[i-1, 0], i - 1
    print(tab)
    seq = list()
    current = tab[-1]
    seq.insert(0, a[int(current[1])])
    while current[1] > 1:
        current = tab[current[1] - 2]
        seq.insert(0, a[int(current[1])])
    print("Value:\t\t{}".format(tab[-1, 0]))
    print("Sequence:\t{}".format(seq))


def main():
    max_non_adjacent_sum([8, 6, 7, 3, 2, 1, 4, 5, 9])


if __name__ == '__main__':
    main()
