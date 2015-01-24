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


def reverseString(str):
	stack = Stack()
	l = list(str)
	for i in l:
		stack.push(i)

	res = ""
	while not stack.isEmpty():
		res = res + stack.pop()

	return res

def pairChecker(str):
	stack = Stack()
	balanced = True
	index = 0
	while index < len(str) and balanced:
		symbol = str[index]
		if symbol == "(":
			stack.push(symbol)
		else:
			if stack.isEmpty():
				balanced = False
			else:
				stack.pop()

		index = index + 1

	if balanced and stack.isEmpty():
		return True
	else:
		return False


def baseConverter(decNumber, base):
	digits = "0123456789ABCDEF"

	stack = Stack()

	while decNumber > 0:
		rem = decNumber % base
		stack.push(rem)
		decNumber = decNumber // base

	newStr = ""
	while not stack.isEmpty():
		newStr = newStr + digits[stack.pop()]

	return newStr




#tests

stack = Stack()
print(stack.isEmpty())
stack.push(4)
stack.push(8)
stack.push(7)
stack.push(2)
print(stack.pop())
print(stack.peek())

print(reverseString("abcdef"))

print(pairChecker("()()()()"))
print(pairChecker("())"))
print(baseConverter(423, 2))

		