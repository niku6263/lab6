import numpy as np

f = lambda x1,x2: 4*x1**2 + x2**2 - 4
g = lambda x1,x2: x1 + x2 - np.sin(x1-x2)

dfx1 = lambda x1,x2: 8*x1
dfx2 = lambda x1,x2: 2*x2
dgx1 = lambda x1,x2: 1 - np.cos(x1-x2)
dgx2 = lambda x1,x2: 1 + np.cos(x1-x2)

Jay = np.array( ((dfx1(1,0),dfx2(1,0)), (dgx1(1,0),dgx2(1,0))) )
J = np.linalg.inv(Jay)

x1n = 1
x2n = 0
tol = 10**-10

print("|n|xn|yn|q|")
for n in range(100):

    F = np.array([[f(x1n,x2n)], [g(x1n,x2n)]])
    L = np.array([[x1n], [x2n]])

    xn1 = x1n
    xn2 = x2n

    Z = L - J@F

    ([[x1n],[x2n]]) = Z

    if(x1n-0.9986069440971734 >= tol and (x2n+0.105530492293077)>=tol):
        q = np.log(abs(xn1-0.5))/np.log(abs(x1n-0.5))
    else:
        q = np.log(abs(xn1-0.5))/np.log(abs(x1n-0.5))
        ko = "Converged Within Tolerance"
        print("|",n,"|",x1n,"|",x2n,"|",q,ko,"|")
        break

    print("|",n,"|",x1n,"|",x2n,"|",q,"|")