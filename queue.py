class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		return self.items.insert(0, item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)


q = Queue()
q.isEmpty()
q.enqueue(6)
q.enqueue(7)
q.enqueue(8)
print(q.dequeue())


def queueGame(players, num):
	simQueue = Queue()
	for player in players:
		simQueue.enqueue(player)

	while simQueue.size() > 1:
		for i in range(num):
			simQueue.enqueue(simQueue.dequeue())
		simQueue.dequeue()

	return simQueue.dequeue()

print(queueGame(["A","B","C","D","E","F","G","H","J"], 3))












