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