from stack import Stack

# selection sort like method
def selection_sort(stack):
    sorted = 0
    aux = Stack()
    while stack:
        min = None
        while stack:
            item = stack.pop()
            if min is None:
                min = item
            elif item < min:
                aux.push(min)
                min = item
            else:
                aux.push(item)
        i = 0
        while i < len(aux) - sorted:
            stack.push(aux.pop())
        aux.push(min)
        sorted += 1
    while aux:
        stack.push(aux.pop())

# insertion sort like method
def insertion_sort(stack):
    aux = Stack()
    while stack:
        tmp = stack.pop()
        while not aux.empty() and tmp < aux.peek():
            stack.push(aux.pop())
        aux.push(tmp)
    while aux:
        stack.push(aux.pop())



import random
seq = list(range(1, 10))
random.shuffle(seq)

stack = Stack()
for val in seq:
    stack.push(val)
print(*stack)
selection_sort(stack)
print(*stack)

stack = Stack()
for val in seq:
    stack.push(val)
insertion_sort(stack)
print(*stack)
        
        
    

    