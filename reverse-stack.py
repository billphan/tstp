# A common programming interview problem - reversing a string using a stack by first putting it in on a stack, then taking it off.

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
        last = len(self.items) - 1
        return self.items[last]

    def size(self):
        return len(self.items)

stack = Stack()
# Goes through each character in text and pushes it to the stack.
for text in "Hello, World!":
    stack.push(text)

reverse = ""
# Iterate through the stack taking letters from text and putting them in reverse variable in reverse order.
for i in range(len(stack.items)):
    reverse += stack.pop()

print(reverse)
