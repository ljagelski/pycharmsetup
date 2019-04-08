import functools

fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

fset = list(set(fibonacci))

print('fset_list1')
print(fset)

fib2 = []

for fib in fibonacci:
    if not fib in fib2:
        fib2.append(fib)

print('f2')
print(fib2)

odd_numbers = list(filter(lambda x: x % 2, fibonacci))
print('Odds')
print(odd_numbers)

print('Evens')
even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))
print(even_numbers)

# even2 = list(filter(lambda x: x % 2 + 1, fibonacci))
# print(even2)

'''
    python 1 is True, 0 is False
'''

class greeter(object):
    '''
    class to display greetings
    '''
    def __init__(self, name):
        self.name = name

    def greet(self, loud = False):
        if loud:
            print('HELLO %s' % self.name.upper())
        else:
            print('Hello %s' % self.name)


tuser = greeter('Fred')

tuser.greet(True)
tuser.greet() #uses default lound = False

#pythagorean triple
print('sqlist')
sqlist = [(x,y,z) for x in range(1,30) for y in range(x, 30) for z in range(y,30) if x**2 + y**2 == z**2]
print(sqlist)

colors = ['red', 'green', 'blue']
things = ['house', 'car', 'bike']
print([(x,y) for x in colors for y in things])

print('list enumerate')
print(list(enumerate(colors)))

print('just enumerate')
print(enumerate(colors))


print([(x,y,z) for x in range(1,3) for y in range(x, 8) for z in range(y,11)])

print([(x,y,z) for x in range(1,5) for y in range(2, 6) for z in range(3,7)])

l1 = [(x,y,z) for x in range(1,5) for y in range(2, 6) for z in range(3,7)]


def print1(itup):
    print('itup: ', itup)


for itup in l1:
    print1(itup)





