import random


def set_cover_bnb(s, sets):
    if set.union(*sets) != s:
        return None
    n = len(sets)
    active = [[i] for i in range(n)]
    best_card = n
    best = n
    while len(active):
        sub = active.pop()
        for i in range(sub[-1] + 1, n):
            nsub = sub + [i]
            if set.union(*[sets[j] for j in nsub]) == s:
                if len(nsub) < best_card:
                    best_card = len(nsub)
                    best = nsub
            elif len(nsub) < best_card:
                active.append(nsub)
    return best_card, best


def main():
    s = set(i for i in range(10))
    sets = list(set(random.sample(range(10), 3)) for i in range(5))
    # sets = [{0, 1, 2, 3, 4}, {4, 5}, {5, 6, 7, 8, 9}]
    ret = set_cover_bnb(s, sets)
    while ret is None:
        s = set(i for i in range(10))
        sets = list(set(random.sample(range(10), 3)) for i in range(5))
        ret = set_cover_bnb(s, sets)
    print(sets)
    print(ret)


if __name__ == '__main__':
    main()
