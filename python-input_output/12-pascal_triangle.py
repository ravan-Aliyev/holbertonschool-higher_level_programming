#!/usr/bin/python3
"""Pascal triangle"""


def pascal_triangle(n):
    """Pascal triangle"""
    if n <= 0:
        return []
    arr = []
    for i in range(1, n):
        num = [j + 1 for j in range(i)]
        num[-1] = num[0]
        # num[i - 1] = num[(i - 1) + (i - 1)]
        if (i > 1):
            num[1] = num[1]
        arr.append(num)
    print(arr)
    return [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]