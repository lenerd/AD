import numpy as np


class Graph:

    def __init__(self, matrix):
        self.matrix = matrix
        self.n = matrix.shape[0]

    def weight(self, a, b):
        return self.matrix[a][b]

    def predecessors(self, a):
        return set(i for i in range(self.n) if self.matrix[i][a] != 0)

    def successors(self, a):
        return set(i for i in range(self.n) if self.matrix[a][i] != 0)

    def __str__(self):
        return str(self.matrix)

    def from_file(filename):
        with open(filename, 'r') as f:
            matrix = np.loadtxt(f, delimiter=' ')
        return Graph(matrix)


def dijkstra_mult(G, s, t):
    S = {s}
    dist = dict()
    dist[s] = 1
    while t not in S and len(S) != G.n:
        U = set()
        for s in S:
            U.update(G.successors(int(s)))
        U = U - S
        if len(U) == 0:
            break
        mind = max(((u, dist[p] * G.weight(p, u))
                    for u in U
                    for p in G.predecessors(u).intersection(S)),
                   key=lambda x: x[1])
        S.add(mind[0])
        dist[mind[0]] = mind[1]
    return dist[t]


def main():
    G = Graph.from_file('matrixA.txt')
    a = (1, 16, dijkstra_mult(G, 0, 15))
    b = (2, 13, dijkstra_mult(G, 1, 12))
    c = (4,  6, dijkstra_mult(G, 3,  5))
    print("Wahrscheinlichkeit von {} zu {}: {}".format(*a))
    print("Wahrscheinlichkeit von {} zu {}: {}".format(*b))
    print("Wahrscheinlichkeit von {} zu {}: {}".format(*c))


if __name__ == '__main__':
    main()
