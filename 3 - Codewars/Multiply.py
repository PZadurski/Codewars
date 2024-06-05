def multiply(n):
    multi = 5 ** len(str(n))
    if n<0:
        multi = 5 ** (len(str(n))-1)
    return n * multi



multiply(-2)


#def multiply(n):
#return n*5**len(str(abs(n)))