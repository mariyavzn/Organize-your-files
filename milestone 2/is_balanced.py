
def is_balanced(symbols):
    stack = []
    for symbol in symbols:
        if symbol == '(':
            stack.append(symbol)
        elif symbol == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return False

    return len(stack) == 0

print(is_balanced('()'))  
print(is_balanced('())'))  
print(is_balanced('(()'))
print(is_balanced(')())'))