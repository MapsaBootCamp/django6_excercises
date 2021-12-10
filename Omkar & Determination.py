def determinable(grid: list, row, col) -> str:
    for elm in grid:
        if 'X.' in elm[row-1: col+1]:
            return "NO"
    return "YES"


n, m = tuple(map(int, input().split(' ')))
grd = []
for i in range(n):
    grd.append(input())

q = int(input())
for i in range(q):
    a, c = tuple(map(int, input().split(' ')))
    print(determinable(grd, a, c))
