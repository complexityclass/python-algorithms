import timeit
import sys

#list generators

N_VALUE = 1000

def test_gen1():
	mList = []
	for i in range(N_VALUE):
		mList = mList + [i]

def test_gen2():
	mList = []
	for i in range(N_VALUE):
		mList.append(i)

def test_gen3():
	mList = [i for i in range(N_VALUE)]

def test_gen4():
	mList = list(range(N_VALUE))

#benchmarks

print(sys.version)

t1 = timeit.Timer("test_gen1", "from __main__ import test_gen1").timeit(N_VALUE)
print("concat \t",t1," \t milliseconds")

t2 = timeit.Timer("test_gen2", "from __main__ import test_gen2").timeit(N_VALUE)
print("append \t",t2," \t milliseconds")

t3 = timeit.Timer("test_gen3", "from __main__ import test_gen3").timeit(N_VALUE)
print("comprehension \t",t3,"\t milliseconds")

t4 = timeit.Timer("test_gen4", "from __main__ import test_gen4").timeit(N_VALUE)
print("list range \t",t4,"\t milliseconds")
