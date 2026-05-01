# a = [0, 1, 2, 3, 4, 5]
# b = iter(a)
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))
# print(next(b))

# It stores the entire list in memory and keeps the track of index

# -----Generators-------
def gen():
    for i in range(6):
        yield i

g = gen()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))

# The generator doesnot store the entire list. It generates values on the fly using yield method



