from functools import reduce

class RopeNode:
    def __init__(self, val: str | None = None, lhs: 'RopeNode | None' = None, rhs: 'RopeNode | None' = None):
        if val is not None:
            self.weight = len(val)
        elif lhs is not None:
            self.weight = lhs.get_lhs_weight()

        self.lhs: 'RopeNode' | None = lhs
        self.rhs: 'RopeNode' | None = rhs

        self.val = val

    def get_lhs_weight(self):
        if self.lhs is not None:
            return self.lhs.get_lhs_weight()
        return self.weight

class Rope:
    def __init__(self, val: str, leaf_size: int):
        self.root = self._to_root([RopeNode(val[i:i+leaf_size]) for i in range(0, len(val), leaf_size)])

    def _to_root(self, nodes):
        new = reduce(lambda lhs, rhs : RopeNode(None, lhs, rhs), nodes)

if __name__ == "__main__":
    thing = [1, 2, 3, 4, 5, 6, 7, 8]

    thing = [x for x in thing]
