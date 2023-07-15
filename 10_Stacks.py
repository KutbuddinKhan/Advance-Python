# Stack
class Stack:
    def __init__(self):
        self.stack = []

    # adding element to the top of the stack
    def push(self, item):
        self.stack.append(item)

    # removing top most item fromt the stack
    def pop(self):
        self.stack.pop()

    # reading the value of t item on the top most stack
    def peek(self):
        last_element = self.stack[len(self.stack) - 1]
        return last_element
    
stack1 = Stack()
stack1.push(5)
stack1.push(4)
stack1.push(3)

print(stack1.peek()) # output: 3

print(stack1.pop())

print(stack1.peek()) # output: 4