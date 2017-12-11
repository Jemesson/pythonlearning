def test():
    yield 1
    for i in range(3):
        yield i


testing = test()
print(testing.__next__())

print(testing.__next__())
print(testing.__next__())
print(testing.__next__())

y = lambda x: x*2
print(y(4))
