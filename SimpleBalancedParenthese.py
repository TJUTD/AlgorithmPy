from DataStructure import Stack  # right click current project to make directory as source root

def par_checker(symbol_string):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                s.pop()

        index += 1

    return balanced and s.is_empty()

print(par_checker('(((((()))))'))
print(par_checker('(()(()))'))