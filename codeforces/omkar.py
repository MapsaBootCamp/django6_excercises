n, m = tuple(map(int, input().split(' ')))
grd = []
for i in range(n):
    grd.append(input())

q = int(input())
l = []
for i in range(q):
    a, c = tuple(map(int, input().split(' ')))
    temp_grid = []
    for elm in grd:
        s = ''
        for j in range(a-1, c):
            s += elm[j]
        temp_grid.append(s)

    # temp_grid = temp_grid[::-1]
    # print(determinable(temp_grid, a, c))
    # print(temp_grid)
    l.append(temp_grid.pop())


# s = set(l)
# print('in l :', l)
for j in range(len(l)):
    if 'X.' in l[j]:
        print('NO')
    else:
        print('Yes')
