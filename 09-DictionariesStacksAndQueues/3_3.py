import queue

# Expressions to be checked
expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}"  # Brackets OK
expression2 = "[(2+3]/4)"                  # Brackets not correct
expression3 = "(2-3*4+(5/6)"               # Brackets not correct

def brackets_ok(expression):
    # Stack to keep track of opening brackets
    stack = []
    # Dictionary to match opening and closing brackets
    brackets = {')': '(', '}': '{', ']': '['}
    
    # Iterate through each character in the expression
    for char in expression:
        # If the character is an opening bracket, push it onto the stack
        if char in "({[":
            stack.append(char)
        # If it's a closing bracket, check for a match
        elif char in ")}]":
            if not stack or stack.pop() != brackets[char]:
                return False  # Mismatch or unbalanced brackets
    
    # If stack is empty, brackets are balanced; otherwise, they are not
    return len(stack) == 0

# Test each expression
if brackets_ok(expression1):
    print(f"Expression 1: Brackets are OK")
else:
    print(f"Expression 1: Brackets are not correct")

if brackets_ok(expression2):
    print(f"Expression 2: Brackets are OK")
else:
    print(f"Expression 2: Brackets are not correct")

if brackets_ok(expression3):
    print(f"Expression 3: Brackets are OK")
else:
    print(f"Expression 3: Brackets are not correct")
