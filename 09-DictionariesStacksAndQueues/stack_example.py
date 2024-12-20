import queue

"""
A stack is a linear data structure that follows
the Last In, First Out (LIFO) principle.
This means the last element added to the stack
is the first one to be removed. Think of a stack
as a pile of plates — the last plate you place
on the top is the first one you'll take off.
"""

# creates a stack
cards = queue.LifoQueue()

# adds elements to the top of the stack
cards.put('King of Hearts \u2665')    
cards.put('Queen of Diamonds \u2666')  
cards.put('Jack of Spades \u2660')     

## prints number of elements of the stack
print('Number of stack elements:', cards.qsize())

# removes and prints elements from the top of the stack
while not cards.empty():
    card = cards.get()
    print(card)

# Stack implementation using a list
stack = []

# Perform the required operations
stack.append(2)  # Push 2 onto the stack
stack.append(3)  # Push 3 onto the stack
stack.append(7)  # Push 7 onto the stack
stack.append(4)  # Push 4 onto the stack
stack.append(1)  # Push 1 onto the stack
stack.append(9)  # Push 9 onto the stack
stack.append(8)  # Push 8 onto the stack

# Sum the last two numbers
last = stack.pop()  # Pop the last number (8)
second_last = stack.pop()  # Pop the second last number (9)
print("Sum of the last two numbers:", last + second_last)

# Calculate the sum of the remaining stack elements
remaining_sum = 0
while stack:
    remaining_sum += stack.pop()  # Pop each element and add to the total
print("Sum of the remaining stack elements:", remaining_sum)


"""
Note the order of the printed elements.
The last added element is printed first.
"""
