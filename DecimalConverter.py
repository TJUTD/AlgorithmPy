from DataStructure import Stack  # right click current project to make directory as source root

def divide_by_2(dec_number):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % 2
        rem_stack.push(rem)
        dec_number //= 2    # // integer division

    bin_string = ""
    while not rem_stack.is_empty():
        bin_string += str(rem_stack.pop())

    return bin_string

def base_converter(dec_number, base):
    rem_stack = Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number //= base    # // integer division

    base_string = ""
    while not rem_stack.is_empty():
        base_string += str(rem_stack.pop())

    return base_string


print(divide_by_2(127))
print(divide_by_2(128))

print(base_converter(256, 2))
print(base_converter(256, 16))