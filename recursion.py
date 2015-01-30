def listSum(numList):
	theSum = 0
	for i in numList:
		theSum = theSum + i
	return theSum

print(listSum([1,2,3,4,5,6]))

def recursionSum(numList):
	if numList == []:
		return 0
	else:
		return numList.pop() + recursionSum(numList)

print(recursionSum([1,2,3,4,5,6]))