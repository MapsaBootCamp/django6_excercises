# from typing import List

# # ---- creating grid with matrix(sakht shabake morede nazar) ----

# rowno = int(input('bgo tol : '))
# colno = int(input('bgo arz : '))

# por = ['x']
# khali = ['.']

# matrix = []

# for m in range(rowno):
#     Listrow = []
#     for k in range(colno):
#         soal = input('mikhay por bashe radife avalet ya khali?(p/kh) ')
#         if soal == 'p':
#             Listrow.append(por[0])
#         elif soal == 'kh':
#             Listrow.append(khali[0])
#     matrix.append(Listrow)

# print('- ' * 15) # joda sazi
# print(rowno, colno) # satr o soton morede nazar
# print(matrix) # shabake morede nazaremon

# # ---- creating subgrid (sakht zir sakht haye morede nazar) ----

# test = int(input('chand bar mikhay test koni? '))

# def foo(matrix):
#     x1 = int(input('arz columni k mikhay cut koni (nabayd az grid bozorgtr bashe) (ba tavajoh b andis) : '))
#     x2 = int(input('tol columni k mikhay cut koni (nabayd az grid bozorgtr bashe) (ba tavajoh be andis): '))
#     por = 'n'
#     khali = 'e'
#     sub_matrix = []
#     flat_list = []
#     for elm in matrix[x1:]:
#         sub_matrix.append(elm)


#     count = len(sub_matrix)
#     while 0 < count:
#         for elm in sub_matrix:
#             a = sub_matrix.pop(0)
#         for elm1 in range(len(a)):
#             if a[elm1] == a[x2]:
#                 flat_list.append(a[elm1])
        
#         count -= 1
    
#     return flat_list


# matrix = [
#         ['.', '.', 'x', 'x', 'x'], 
#         ['.', '.', '.', 'x', '.'],
#         ['.', '.', '.', 'x', '.'],
#         ['.', '.', '.', 'x', '.']
#         ]

# for elm in range(test):
#     print(foo(matrix))



def determinable(temp_grid: list, row, col) -> str:
    pass
    
    


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
    print(temp_grid)
    l.append(temp_grid.pop())


s = set(l)
print('in l :', l)
for j in range(len(l)):
    if 'X.' in l[j]:
        print('NO')
    else:
        print('Yes')
