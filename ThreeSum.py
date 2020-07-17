print('hello')

target = 0
array = [12, 3, 1, 2, -6, 5, -8, 6]
array_sorted = sorted(array)

i = 0
array_left = []
array_right = []

for i in array_sorted:
    if i < target:
        array_left.append(i)
    elif i >= target:
        array_right.append(i)


print(array_left)
print(array_right)

p1 = 0
p2 = len(array_right) - 1



combo = []

for i in array_left:
    while p1 < p2:
        print('loop')
        print('i: ' + str(i))
        print('p1 val: ' + str(array_right[p1]))
        print('p2 val: ' + str(array_right[p2]))

        if (array_right[p1] + array_right[p2] + i) == target:
            combo.append([i, array_right[p1], array_right[p2]])
            # keep moving toward center
            p2 = p2 - 1
            p1 = p1 + 1
        elif (array_right[p1] + array_right[p2] + i) > target:
            # move sum left
            p2 = p2 - 1
        elif (array_right[p1] + array_right[p2] + i) < target:
            # move sum left
            p1 = p1 + 1

    # restart this for next i
    p1 = 0
    p2 = len(array_right) - 1


print(combo)
