import math


def checkio(data):
    a, b = data
    size = math.ceil(math.sqrt(max(data)))
    M = [[0] * size for _ in range(size)]

    # insert values
    i = j = 0
    v, d = size ** 2, 'down'
    M[i][j] = v
    directions = {
        'up': [-1, 0],
        'down': [1, 0],
        'right': [0, 1],
        'left': [0, -1],
    }

    while v > 1:
        v -= 1
        d_coords = directions[d]
        i += d_coords[0]
        j += d_coords[1]
        M[i][j] = v
        # change direction
        if d == 'down':
            if i + 1 >= size or M[i + 1][j] != 0:
                d = 'right'
        elif d == 'right':
            if j + 1 >= size or M[i][j + 1] != 0:
                d = 'up'
        elif d == 'up':
            if i - 1 < 0 or M[i - 1][j] != 0:
                d = 'left'
        elif d == 'left':
            if j - 1 < 0 or M[i][j - 1] != 0:
                d = 'down'

    # get indexes elements
    for i, item in enumerate(M):
        if a in item:
            a_coords = [i, item.index(a)]
        if b in item:
            b_coords = [i, item.index(b)]

    # calculate number of steps
    distance = sum(map(lambda x, y: abs(x-y), a_coords, b_coords))

    return distance


#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([1, 9]) == 2, "First"
    assert checkio([9, 1]) == 2, "Reverse First"
    assert checkio([10, 25]) == 1, "Neighbours"
    assert checkio([5, 9]) == 4, "Diagonal"
    assert checkio([26, 31]) == 5, "One row"
    assert checkio([50, 16]) == 10, "One more test"
    assert checkio([4, 1]) == 1, "!!!"