test = int(input('chand bar mikhay test koni? '))

def show_rect():
    '''
    m and n are lenght and height
    in this problem we do mathematical operations
    our criterion is Space(masaht) in the area
    '''
    m = int(input('tol mostatilet chand bashe? '))
    n = int(input('arz mostatilet chand bashe? '))
    masahat = m * n
    new_rect = masahat / 3
    if m == 1 and n == 1:
        return 1
    elif m % 2 == 0 and n % 2 == 0:
        return int(masahat/2)
    elif masahat % 2 == 0:
        return int((masahat/2) - 1)
    else:
        return int(new_rect) 


for elm in range(test):
    print(show_rect())