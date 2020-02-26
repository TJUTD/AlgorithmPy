class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next

class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        # assume the item is not already in the list
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item):
        # assume the item is present in the list
        curr = self.head
        prev = None
        found = False
        while not found:
            if curr.get_data() == item:
                found = True
            else:
                prev = curr
                curr = curr.get_next()
        if prev == None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    def search(self, item):
        curr = self.head
        found = False
        while curr != None and not found:
            if curr.get_data() == item:
                found = True
            else:
                curr = curr.get_next()
        return found

    def is_empty(self):
        return self.head == None

    def size(self):
        curr = self.head
        cnt = 0
        while curr != None:
            cnt += 1
            curr = curr.get_next()
        return cnt


    def append(self, item):
        temp = Node(item)
        curr = self.head
        while curr.get_next() != None:
            curr = curr.get_next()
        curr.set_next(temp)

    def index(self, item):
        # assume the item is in the list
        curr = self.head
        pos = 0
        while curr.get_data() != item:
            pos += 1
            curr = curr.get_next()
        return pos

    def pop(self, pos=None):
        curr = self.head
        # assume the list has at least one item
        if pos == None:
            if curr.get_next() == None:
                self.head = None
                return curr.get_data()
            else:
                prev = curr
                curr = curr.get_next()
                while curr.get_next() != None:
                    prev = curr
                    curr = curr.get_next()
                prev.set_next(None)
                return curr.get_data()

        # assume the item is in the list
        else:
            for i in range(pos):
                curr = curr.get_next()
                self.remove(curr.get_data())
            return curr.get_data()

    def __str__(self):
        list_str = "head"
        curr = self.head
        while curr != None:
            list_str = list_str + "->" + str(curr.get_data())
            curr = curr.get_next()
        list_str = list_str + "->" + str(None)
        return list_str

# l = UnorderedList()
# l.add(1)
# l.add(3)
# l.append(5)
# l.append(7)
# print(l)
# print(l.is_empty())
# print(l.size())
# print(l.index(1))
# print(l.index(3))
# print(l.index(5))
# print(l.index(7))
# print(l.pop(0))


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        # assume the item is not already in the list
        curr = self.head
        prev = None
        stop = False
        while curr != None and not stop:
            if curr.get_data() > item:
                stop = True
            else:
                prev = curr
                curr = curr.get_next()

        temp = Node(item)
        if prev == None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(curr)
            prev.set_next(temp)

    def remove(self, item):
        # assume the item is present in the list
        curr = self.head
        prev = None
        found = False
        while not found:
            if curr.get_data() == item:
                found = True
            else:
                prev = curr
                curr = curr.get_next()
        if prev == None:
            self.head = curr.get_next()
        else:
            prev.set_next(curr.get_next())

    def search(self, item):
        curr = self.head
        found = False
        stop = False
        while curr != None and not found and not stop:
            if curr.get_data() == item:
                found = True
            else:
                if curr.get_data() > item:
                    stop = True
                else:
                    curr = curr.get_next()
        return found

    def is_empty(self):
        return self.head == None

    def size(self):
        curr = self.head
        cnt = 0
        while curr != None:
            cnt += 1
            curr = curr.get_next()
        return cnt

    def index(self, item):
        # assume the item is in the list
        curr = self.head
        pos = 0
        while curr.get_data() != item:
            pos += 1
            curr = curr.get_next()
        return pos

    def pop(self, pos=None):
        curr = self.head
        # assume the list has at least one item
        if pos == None:
            if curr.get_next() == None:
                self.head = None
                return curr.get_data()
            else:
                prev = curr
                curr = curr.get_next()
                while curr.get_next() != None:
                    prev = curr
                    curr = curr.get_next()
                prev.set_next(None)
                return curr.get_data()

        # assume the item is in the list
        else:
            for i in range(pos):
                curr = curr.get_next()
                self.remove(curr.get_data())
            return curr.get_data()

    def __str__(self):
        list_str = "head"
        curr = self.head
        while curr != None:
            list_str = list_str + "->" + str(curr.get_data())
            curr = curr.get_next()
        list_str = list_str + "->" + str(None)
        return list_str

# l = OrderedList()
# l.add(10)
# l.add(100)
# l.add(50)
# l.add(30)
# print(l)
# print(l.is_empty())
# print(l.size())
# print(l.index(100))
# print(l.pop(1))
# print(l.pop())

class HashTable:
    def __init__(self, sz=11, skip=1):
        self.size = sz
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.skip = skip

    def put(self, key, data):
        hash_val = self.hash_fun(key, self.size)

        if self.slots[hash_val] == None:
            self.slots[hash_val] = key
            self.data[hash_val] = data
        else:
            if self.slots[hash_val] == key:
                self.data[hash_val] = data
            else:
                next_slot = self.rehash(hash_val, self.size, self.skip)
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, self.size, self.skip)
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    def get(self, key):
        start_slot = self.hash_fun(key, self.size)
        data = None
        stop = False
        found = False
        pos = start_slot

        while self.slots[pos] != None and not found and not stop:
            if self.slots[pos] == key:
                found =True
                data = self.data[pos]
            else:
                pos = self.rehash(pos, self.size, self.skip)
                if pos == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, value):
        self.put(key, value)

    def hash_fun(self, key, size):
        return key % size

    def rehash(self, old_hash, size, skip):
        return (old_hash + skip) % size


# h = HashTable()
# h[54] = "a"
# h[26] = "b"
# h[93] = "c"
# h[17] = "d"
# h[77] = "e"
# h[31] = "f"
# h[44] = "g"
# h[55] = "h"
# h[20] = "i"
# print(h.slots)
# print(h.data)
# h[20] = "j"
# print(h[20])
# print(h.data)


def binary_tree(r):
    return [r, [], []]

def insert_left(root, leaf):
    lc = root.pop(1)
    if len(lc) > 1:
        root.insert(1, [leaf, lc, []])
    else:
        root.insert(1, [leaf, [], []])

def insert_right(root, leaf):
    rc = root.pop(2)
    if len(rc) > 1:
        root.insert(2, [leaf, [], rc])
    else:
        root.insert(2, [leaf, [], []])

def get_root_val(root):
    return root[0]

def set_root_val(root, val):
    root[0] = val

def get_left_child(root):
    return root[1]

def get_right_child(root):
    return root[2]

# r = binary_tree(5)
# insert_left(r, 1)
# insert_left(r, 2)
# insert_right(r, 6)
# insert_right(get_left_child(r), 3)
# print(r)

class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, val):
        if self.left_child == None:
            self.left_child = BinaryTree(val)
        else:
            tmp = BinaryTree(val)
            tmp.left_child = self.left_child
            self.left_child = tmp

    def insert_right(self, val):
        if self.right_child == None:
            self.right_child = BinaryTree(val)
        else:
            tmp = BinaryTree(val)
            tmp.right_child = self.right_child
            self.right_child = tmp

    def get_root_val(self):
        return self.key

    def set_root_val(self, val):
        self.key = val

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


# def preorder(tree):
#     if tree:
#         print(tree.get_root_val())
#         preorder(tree.get_left_child())
#         preorder(tree.get_right_child())
#
# def inorder(tree):
#     if tree:
#         inorder(tree.get_left_child())
#         print(tree.get_root_val())
#         inorder(tree.get_right_child())
#
# def postorder(tree):
#     if tree:
#         postorder(tree.get_left_child())
#         postorder(tree.get_right_child())
#         print(tree.get_root_val())

# t = BinaryTree('a')
# t.insert_left('b')
# t.insert_right('c')
# print(t.get_root_val())
# print(t.get_left_child().get_root_val())
# print(t.get_right_child().get_root_val())
# preorder(t)
# inorder(t)
# postorder(t)

class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.size = 0

    def perc_up(self, i):
        while i // 2 > 0:
            if self.heap_list[i] < self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i//2], self.heap_list[i]
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.size += 1
        self.perc_up(self.size)

    def min_child(self, i):
        if i * 2 + 1 > self.size:
            return i * 2
        else:
            if self.heap_list[i*2] < self.heap_list[i*2+1]:
                return i * 2
            else:
                return i * 2 + 1

    def perc_down(self, i):
        while i*2 <= self.size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
            i = mc

    def del_min(self):
        val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.size]
        self.size -= 1
        self.heap_list.pop()
        self.perc_down(1)
        return val

    def build_heap(self, lst):
        i = len(lst) // 2
        self.size = len(lst)
        self.heap_list = [0] + lst[:]
        while i > 0:
            self.perc_down(i)
            i -= 1

# bh = BinaryHeap()
# bh.insert(5)
# bh.insert(4)
# bh.insert(3)
# bh.insert(2)
# bh.insert(1)
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
# bh = BinaryHeap()
# bh.build_heap([9,7,5,3,1])
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
# print(bh.del_min())
