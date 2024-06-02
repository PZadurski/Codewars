def collinearity(x1,x2,y1,y2):
    if x1==0 and y1==0:
        return True
    if x2==0 and y2==0:
        return True

    if x1!=0 and x2!=0:
        if y1!=0 and y2!=0:
            z1 = x1/y1
            z2 = x2/y2
            if z1==z2:
                return True
            else:
                return False

    if (x1==0 and x2==0) or (y1==0 and y2==0):
        return True

    return False

#   def collinearity(x1, y1, x2, y2):
#     return x1 * y2 == x2 * y1

x1=5
x2=7
y1=0
y2=0
collinearity(x1,x2,y1,y2)
