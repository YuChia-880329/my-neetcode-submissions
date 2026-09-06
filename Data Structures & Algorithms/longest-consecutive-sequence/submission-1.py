class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class UFNode:
            def __init__(self, num):
                self.num = num
                self.parent = self
                self.rank = 0
                self._size = 1

            def find(self):
                # path compression
                if self.parent is not self:
                    self.parent = self.parent.find()
                return self.parent

            @ staticmethod
            def _link(x, y):
                # union by rank
                if x.rank < y.rank:
                    x.parent = y
                    y._size += x._size
                else:
                    y.parent = x
                    x._size += y._size
                    if x.rank == y.rank:
                        x.rank += 1

            def union(self, y):
                UFNode._link(self.find(), y.find())

            @property
            def size(self):
                return self.find()._size

        record = {}
        max_size = 0
        for num in nums:
            if num not in record:
                record[num] = UFNode(num)
            x = record[num].find()
            if num-1 in record:
                y = record[num-1].find()
                if x is not y:
                    x.union(y)
            if num+1 in record:
                y = record[num+1].find()
                if x is not y:
                    x.union(y)
            if record[num].size > max_size:
                max_size = record[num].size

        return max_size
