def multiples_3_5():
    # This was a brute force approach, not the mathematical one the
    # problem intended; done long ago but leaving it in the commit
    # for purposes of completion.
    return sum([i for i in range(1, 1000) if i % 3 == 0 or i % 5 == 0])

print(multiples_3_5())
