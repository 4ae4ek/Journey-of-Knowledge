class Tree:
    def __init__(self, size=0, name=None, typeF='dir'):
        self.size = size
        self.children = []
        self.parent = None
        self.name = name
        self.typeF = typeF

    def __str__(self):
        return f'{self.name} {self.size} {self.children} {self.typeF}'

    def _add_size(self, size):
        self.size += size
        if self.parent is not None:
            self.parent._add_size(size)

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
        self._add_size(child.size)

    def calc_answer(self):
        if self.typeF == 'dir' and self.size <= 100000:
            sz = self.size
            total.append(sz)
        if self.children:
            for ch in self.children:
                ch.calc_answer()

    def calc_answer_2(self):
        if self.typeF == 'dir':
            total_2.append(self.size)
        if self.children:
            for ch in self.children:
                ch.calc_answer_2()


tree = Tree(0, name='/')

with open('input.txt', 'r') as f:
    current_dir = tree
    counter = 0
    for l in f:
        counter += 1
        if counter == 1 or counter == 2:
            continue
        l = l.strip()
        if l[0] == '$':
            command = l[2]
            if command == 'c':
                dir_k = l[5:]
                if dir_k == '..':
                    current_dir = current_dir.parent
                    continue
                for tr in current_dir.children:
                    f = True
                    if dir_k == tr.name and tr.typeF == 'dir':
                        current_dir = tr
                        f = False
                        break
            if command == 'l':
                continue
        if l[:3] == 'dir':
            dir_k = l[4:]
            f1 = True
            for tr in current_dir.children:
                if dir_k == tr.name and tr.typeF == 'dir':
                    f1 = False
            if f1:
                current_dir.add_child(Tree(0, name=dir_k))
        if l[0].isdigit():
            st = l.split()
            dir_k = st[1]
            current_dir.add_child(Tree(int(st[0]), name=dir_k, typeF='file'))

total = []
total_2 = []
total_space = 70000000
need = 30000000
need_to_delete = abs(total_space - tree.size - need)
tree.calc_answer()
tree.calc_answer_2()
print(sum(total))
print(min([i for i in total_2 if i >= need_to_delete]))
