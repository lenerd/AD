import numpy as np


def floyd_warshall(W):
    n = W.shape[0]
    D = list()
    D.append(W.copy())
    P = np.zeros(W.shape, dtype=int)
    for u in range(n):
        for v in range(n):
            if u == v or W[u][v] == float('inf'):
                P[u][v] = -1
            else:
                P[u][v] = u
    for k in range(1, n + 1):
        D.append(np.zeros((n, n)))
        for s in range(n):
            for t in range(n):
                D[k][s][t] = min(D[k-1][s][t], D[k-1][s][k-1] + D[k-1][k-1][t])
                if D[k][s][t] != D[k-1][s][t]:
                    P[s][t] = P[k-1][t]
    if min(D[-1].diagonal()) < 0:
        print("Graph contains negative cycles")
    return (D[-1], P)


def path(P, u, v):
    if u == v:
        return [u, ]
    elif P[u][v] == -1:
        print("there is no path from {} to {}".format(u, v))
    else:
        p = path(P, u, P[u][v])
        p.append(v)
        return p


def main():
    W = np.array([[0, 3, 8, float('inf'), -4],
                  [float('inf'), 0, float('inf'), 1, 7],
                  [float('inf'), 4, 0, float('inf'), float('inf')],
                  [2, float('inf'), -5, 0, float('inf')],
                  [float('inf'), float('inf'), float('inf'), 6, 0]])
    D = floyd_warshall(W)
    print(D[0])
    print(D[1])
    print(path(D[1], 0, 3))
    for u in range(W.shape[0]):
        for v in range(W.shape[0]):
            print("path from {} to {}:".format(u, v))
            print(path(D[1], u, v))


if __name__ == '__main__':
    main()
