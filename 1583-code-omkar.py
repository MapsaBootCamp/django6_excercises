import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(input())[: -1] for _ in range(n)]
 
table = [0] * (m + 1)
for i in range(n - 1):
  for j in range(m - 1):
    if a[i + 1][j] == a[i][j + 1] == "X": table[j + 1] = 1
 
for j in range(m): table[j + 1] += table[j]
 
for _ in range(int(input())):
  l, r = map(int, input().split())
  if table[r - 1] - table[l - 1] == 0:
    print("YES")
  else:
    print("NO")



