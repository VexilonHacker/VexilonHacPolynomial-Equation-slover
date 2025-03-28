# √
import sys
from math import sqrt
version = 2.0
while True:
    bar = "################################################"
    
    try:
        a = float(input("a: "))
        b = float(input("b: "))
        c = float(input("c: "))
    except ValueError:
        print("Data Error: Enter valid numbers Bro :) ")
        sys.exit(0)

    sign_b = "+" if b >= 0 else "-"
    sign_c = "-" if c < 0 else "+"
    
    print("Polynom : {}x² {} {}x {} {} = 0".format(int(a), sign_b, abs(int(b)), sign_c, abs(int(c))))

    delta = b**2 - 4*a*c
    b_ne = -b
    a2 = 2*a

    print("Delta =", delta)

    if delta < 0:
        print("S = {0}")
    elif delta == 0:
        s0 = b_ne / a2
        print("Solution of p(x): S = {" + str(s0) + "}")
    else:
        sqrt_delta = sqrt(delta)
        s_n1_0 = b_ne - sqrt_delta
        s_n1_1 = s_n1_0 / a2
        s_p1_0 = b_ne + sqrt_delta
        s_p1_1 = s_p1_0 / a2
        print("Solution of p(x): S = {" + str(s_p1_1) + " ; " + str(s_n1_1) + "}")

    print(bar)
    ex = input("Exit (y/n): ")
    
    if ex.upper() == "Y":
        print("Good Bye :)")
        print(bar)
        sys.exit(0)
    else: 
        print(bar)
