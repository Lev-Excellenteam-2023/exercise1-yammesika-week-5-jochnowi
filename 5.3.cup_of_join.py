def join(*args, sep="-"):
    result = []
    for arg in args:
        result += arg
        result.append(sep)
    result.pop()
    return result


print(join([1, 2], [8], [9, 5, 6], sep='@'))