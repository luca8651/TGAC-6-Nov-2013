def divide_it(x, y):
    try:
        out = x / y
    except:
        print '   Divide by zero!'
        out = None
    return out

def divide_it1(x,y):
    return x/y

divide_it(4,2)
divide_it(4,0)
