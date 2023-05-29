def interleave(*iterables):
    result = []
    for i in range(len(iterables[0])):
        for j in range(len(iterables)):
            result.append(iterables[j][i])
    return result


print(interleave('abc', [1, 2, 3], ('!', '@', '#')))