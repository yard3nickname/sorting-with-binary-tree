class Node:
    def __init__(self, val):
        self.val = val
        self.l_node = None
        self.r_node = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            node = self.root
            pnode = self.root
            while node:
                if val < node.val:
                    pnode = node
                    node = node.l_node
                else:
                    pnode = node
                    node = node.r_node
            else:
                if val < pnode.val:
                    pnode.l_node = Node(val)
                else:
                    pnode.r_node = Node(val)

    def remove(self, val):
        pass

    def to_list(self):
        def iterate(node):
            if node.l_node:
                iterate(node.l_node)

            res.append(node.val)

            if node.r_node:
                iterate(node.r_node)

        res = []
        if self.root:
            iterate(self.root)
        return res


class Solution:
    def sort(self, list_kn):
        """
        sort given list of sorted sub-lists into sorted list
        :param list_kn: list[list[int]]
        :return: list[int]
        """
        btree = BinaryTree()
        for k in range(len(list_kn)):
            for n in range(len(list_kn[k])):
                btree.add(list_kn[k][n])

        return btree.to_list()


sol = Solution()
sol.sort([[1, 2, 3], [2, 3, 4], [-9, 3, 8]])
