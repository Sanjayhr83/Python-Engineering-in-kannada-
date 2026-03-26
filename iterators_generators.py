"""
1. What is an Iterator?
An iterator is an object that allows you to traverse through a sequence (like list, tuple, string) one element at a time.

Behind the scenes, Python uses two special methods:

__iter__() → returns the iterator object.
__next__() → returns the next item from the sequence.
"""
print("Iterators : ")
numbers = [1, 2, 3]

# Get iterator from list
it = iter(numbers)
print(next(it))  # 1
print(next(it))  # 2
print(next(it))  # 3
# print(next(it))  # Raises StopIteration

#Using Iterators with Loops
for num in [1, 2, 3]:
    print(num)

# Creating Your Own Iterator
# You can define your own class and implement __iter__() and __next__().
class CountDown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        num = self.start
        self.start -= 1
        return num

cd = CountDown(5)
for i in cd:
    print(i)


"""
2. Generators in Python
Writing iterators manually can be complex.
Python provides generators to make this easy.
A generator is a function that uses the keyword yield instead of return
"""
print("Generators : ")
def simple_gen():
    yield 1
    yield 2
    yield 3
gen = simple_gen()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


#Generators with Loops
def squares(n):
    for i in range(n):
        yield i * i
for val in squares(5):
    print(val)

#Generator Expressions
# Like list comprehensions, but use () instead of [].
# They are memory-efficient because values are generated on the fly.
gen_exp = (x*x for x in range(5))
print(next(gen_exp))  # 0
print(next(gen_exp))  # 1
print(list(gen_exp))  # [4, 9, 16]


"""
✨ Summary
Iterators = objects that follow __iter__() and __next__().
Generators = simple way to create iterators using yield.
Generator expressions = memory-efficient, on-demand sequences.
Very useful in handling large datasets, streams, and infinite sequences.
"""