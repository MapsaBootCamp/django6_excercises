def color_count(n: int, m: int):
    area = n * m

    if area % 3 == 0:
        return area // 3
    else:
        return (area // 3) + 1


t = int(input())
for i in range(t):
    n, m = tuple(map(int, input().split(' ')))
    print(color_count(n, m))
