n = int(input("TEDAD SATR RA VARED KONID : "))
m = int(input("TEDAD SOTOON RA VARED KONID : "))
ls_r = []
for i in range(n):
    ls_r.append(input(". or X vared konid : "))
print (ls_r)
matr = [0,0]
ac = 0
 
 
for j in range(1,m):
    for i in range(n-1):
        
        if ls_r[i][j]=='X' and ls_r[i+1][j-1]=='X':
            ac+=1
            break
    matr.append(ac)
print(matr)
k=int(input("TEDAD DARKHAST RA VARED KONID : "))
for i in range(k):
    a = int(input("shomare satr ra vared konid : "))
    b = int(input("shomare sotoon ra vared konid : "))
    if matr[b]-matr[a]==0 :
        print("YES" )
    else :
        print("NO")