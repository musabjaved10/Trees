class B_Tree:
    def __init__(self, data):
        self.data = data
        self.lc = None
        self.rc = None

    def add_lc(self, item):
        assert self.lc is None, "left child exists"
        new = B_Tree(item)
        self.lc = new

    def add_lc(self, item):
        assert self.rc is None, "right child exists"
        new = B_Tree(item)
        self.rc = new

    def del_lc(self):
        assert self.lc is not None, "Left child doesn't exist"
        assert self.lc.lc is None and self.lc.rc is None, "It a parent of someone"
        x = self.lc.data
        self.lc = None
        return x

    def del_rc(self):
        assert self.rc is not None, "Left child doesn't exist"
        assert self.rc.lc is None and self.rc.rc is None, "It a parent of someone"
        x = self.rc.data
        self.rc = None
        return x

    def traverse_pre(self):
        print(self.data, end=" ")
        if self.lc is not None:
            self.lc.traverse_pre()
        if self.rc is not None:
            self.rc.traverse_pre()

    def traverse_in(self):
        if self.lc is not None:
            self.lc.traverse_in()
        print(self.data, end=" ")
        if self.rc is not None:
            self.rc.traverse_in()

    def traverse_post(self):
        if self.lc is not None:
            self.lc.traverse_post()
        if self.rc is not None:
            self.rc.traverse_post()
        print(self.data, end=' ')

    def traverse_bf(self):
        nodes = [self]
        print(self.data, end=' ')
        while nodes:
            p = nodes.pop(0)
            if p.lc is not None:
                print(p.lc.data,end = ' ')
                nodes.append(p.lc)
            if p.rc is not None:
                print(p.rc.data, end=" ")
                nodes.append(p.rc)


node1 = B_Tree("A")
node2 = B_Tree("B")
node3 = B_Tree("C")
node4 = B_Tree("D")
node5 = B_Tree("E")
node6 = B_Tree("F")
node7 = B_Tree("G")

node2.lc = node3
node2.rc = node4

node5.lc = node6
node5.rc = node7

node1.lc = node2
node1.rc = node5


print("In Order : ", end=" ")
node1.traverse_in()
print()
print("Pre Order : ", end=" ")
node1.traverse_pre()
print()
print("Post Order : ", end=' ')
node1.traverse_post()
print()
print("Breadth First : ", end=' ')
node1.traverse_bf()