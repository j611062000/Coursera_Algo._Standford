def karatsuba(x, y):

    if x < 10 or y < 10:
        return x*y

    numOfDigits = max(len(str(x)), len(str(y))) // 2
    bm = 10**numOfDigits

    x1 = x // bm
    x0 = x % bm
    y1 = y //bm
    y0 = y % bm

    z2 = karatsuba(x1, y1)
    z0 = karatsuba(x0, y0)
    z1 = karatsuba((x1 + x0), (y1 + y0)) - z2 - z0

    return z2*bm**2 + z1*bm + z0

x=3141592653589793238462643383279502884197169399375105820974944592
y=2718281828459045235360287471352662497757247093699959574966967627

"""
test case
"""
if karatsuba(x, y) == x*y:
    print("True",x*y)
else:
    print("False, should be {}, rather than {}".format(x*y,karatsuba(x,y)) )
