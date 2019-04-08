# generators.py
def chain(iterable_one, iterable_two):
    for item in iterable_one:
       yield item

    for item in iterable_two:
        yield item

def compress(iterable, mask):
    for index, el in enumerate(iterable):
        if mask[index] == True:
            yield el

def cycle(iterable):
    while True:
        for item in iterable:
            yield item

# compress(["Ivo", "Rado", "Panda"], [False, False, True])
# print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
my_list = cycle([1, 2])
for x in range(0,8):
    print(my_list.__next__())