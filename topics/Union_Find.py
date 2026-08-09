class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))   # each node starts as its own parent
        self.rank = [0] * n            # tracks tree depth, for optimization

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])   # path compression
        return self.parent[x]

    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x == root_y:
            return False   # already connected

        # union by rank: attach smaller tree under bigger one
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x
        self.parent[root_y] = root_x
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1
        return True

    def connected(self, x, y):
        return self.find(x) == self.find(y)


uf = UnionFind(6)
uf.union(0, 1)
uf.union(1, 2)
uf.union(3, 4)

print(uf.connected(0, 2))   # True (0-1-2 all merged)
print(uf.connected(0, 3))   # False
print(uf.connected(3, 4))   # True
