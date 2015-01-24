class Stack:

	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def push(self, item):
		self.items.append(item)

	def pop(self):
		return self.items.pop()

	def peek(self):
		return self.items[len(self.items) - 1]

	def size(self):
		return len(self.items)


#tests

stack = Stack()
print(stack.isEmpty())
stack.push(4)
stack.push(8)
stack.push(7)
stack.push(2)
print(stack.pop())
print(stack.peek())
		