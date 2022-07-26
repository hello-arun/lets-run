class quick_union_wighted:
    """
        id contains root information of each number initially id of each number is
        number itself!
    """

    def __init__(self, N):
        self.id = [0]*N
        self.sz = [1]*N
        for i in range(N):
            self.id[i] = i

    def root(self, i: int):
        while(i != self.id[i]):
            i = self.id[i]
        return i

    def connected(self, p: int, q: int):
        return self.root(p) == self.root(q)

    def union(self, p: int, q: int):
        """
            change root of p to root of q
        """
        i = self.root(p)
        j = self.root(q)
        if (i == j):
            return
        if (self.sz[i] < self.sz[j]):
            self.id[i] = j
            self.sz[j] += self.sz[i]
        else:
            self.id[j] = i
            self.sz[i] += self.sz[j]
