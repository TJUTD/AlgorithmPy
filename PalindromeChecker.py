from DataStructure import Deque

def pal_checker(str):
    char_deque = Deque()

    for ch in str:
        char_deque.add_front(ch)

    eq = True

    while char_deque.size() > 1 and eq:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            eq = False
    return eq

print(pal_checker("asd"))
print(pal_checker("asdfghgfdsa"))