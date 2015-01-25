import random


def max_pow_prod(a, r):
    a = sorted(a, reverse=True)
    r = sorted(r, reverse=True)
    val = 1
    for i in range(len(a)):
        val *= a[i] ** r[i]
    return val


def max_pow_prod_alt(a, r):
    random.shuffle(a)
    random.shuffle(r)
    val = 1
    for i in range(len(a)):
        val *= a[i] ** r[i]
    return val


def main():
    a = random.sample(range(1, 100), 99)
    r = random.sample(range(1, 100), 99)
    sorted_val = max_pow_prod(a, r)
    print(sorted_val)

    max_val = 0
    for i in range(10000):
        val = max_pow_prod_alt(a, r)
        if val > max_val:
            max_val = val
            if max_val > sorted_val:
                print(max_val)

    print(max_val > sorted_val)

if __name__ == '__main__':
    main()
