from functools import singledispatch


@singledispatch
def count_down(arg):
    if not isinstance(arg, (str, tuple, set,
                            int, float, dict)):
        raise ValueError

    for k in range(len(arg)):
        print(''.join(arg))
        arg.pop()


@count_down.register(str)
@count_down.register(tuple)
@count_down.register(set)
def count_down(arg: str):
    count_down(list(arg))


@count_down.register(int)
@count_down.register(float)
def count_down(arg):
    count_down(list(str(arg)))


@count_down.register
def count_down(arg: dict):
    count_down(list(dict.keys()))
