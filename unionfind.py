"""
to Python:
Java UnionFind/Disjoint Set data structure implementation made by William Fiset
https://github.com/williamfiset/Algorithms/blob/master/src/main/java/com/williamfiset/algorithms/datastructures/unionfind/UnionFind.java
"""


class UnionFind:

    def __init__(self, size):

        if size <= 0:
            raise ValueError('Value should be larger than zero')
        self.size = size
        self.numComponents = size

        # initializing arrays with [None]*size is slightly faster
        self.ID = [i for i in range(size)]
        self.SZ = [1 for _ in range(size)]

    def find(self, p):

        root = p
        while root != self.ID[root]:
            root = self.ID[root]

        while p != root:
            next = self.ID[p]
            self.ID[p] = root
            p = next

        return root

    def connected(self, p, q):
        return self.find(p) == self.find(q)

    def componentSize(self, p):
        return self.sz[self.find(p)]

    def size(self):
        return self.size

    def components(self):
        return self.numberComponents

    def unify(self, p, q):

        if self.connected(p,q):
            return

        root1 = self.find(p)
        root2 = self.find(q)

        if self.SZ[root1] < self.SZ[root2]:
            self.SZ[root2] += self.SZ[root1]
            self.ID[root1] = root2
            self.SZ[root1] = 0
        else:
            self.SZ[root1] += self.SZ[root2]
            self.ID[root2] = root1
            self.SZ[root2] = 0

        self.numComponents -= 1