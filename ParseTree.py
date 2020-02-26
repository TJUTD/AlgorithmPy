from DataStructure import Stack
from DataStructure import BinaryTree

def build_parse_tree(mathexp):
    tokens = mathexp.split()
    p_stack = Stack()
    e_tree = BinaryTree('')
    p_stack.push(e_tree)
    curr = e_tree
    for t in tokens:
        if t == '(':
            curr.insert_left('')
            p_stack.push(curr)
            curr = curr.get_left_child()
        elif t not in ['+', '-', '*', '/', ')']:
            curr.set_root_val(int(t))
            curr = p_stack.pop()
        elif t in ['+', '-', '*', '/']:
            curr.set_root_val(t)
            curr.insert_right('')
            p_stack.push(curr)
            curr = curr.get_right_child()
        elif t == ')':
            curr = p_stack.pop()
        else:
            raise ValueError
    return e_tree

import operator
def evaluate(parse_tree):
    opers = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    left = parse_tree.get_left_child()
    right = parse_tree.get_right_child()

    if left and right:
        fn = opers[parse_tree.get_root_val()]
        return fn(evaluate(left), evaluate(right))
    else:
        return parse_tree.get_root_val()

def print_exp(parse_tree):
    str_val = ""
    if parse_tree:
        str_val = '(' + print_exp(parse_tree.get_left_child())
        str_val += str(parse_tree.get_root_val())
        str_val += print_exp(parse_tree.get_right_child()) + ')'
    return str_val

pt = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(pt))
print(print_exp(pt))



