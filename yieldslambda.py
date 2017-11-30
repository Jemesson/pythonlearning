def test():
    yield 1
    for i in range(3):
        yield i


testing = test()
print(testing.__next__())

print(testing.__next__())
print(testing.__next__())
print(testing.__next__())

print(lambda x: x*2)
