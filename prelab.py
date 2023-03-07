import numpy as np

h = 0.01 * 2.**(-np.arange(0,10))

f = lambda x: np.cos(x)

x = np.pi/2

ff = np.zeros(10)
fc = np.zeros(10)

for i in range(10):
    ff[i] = (f(x+h[i])-f(x))/h[i]
    fc[i] = (f(x+h[i])-f(x-h[i]))/(2*h[i])

print("Values for Forward Difference are as follows for given values of h: ", ff)
print("Likewise for the Centered Difference: ", fc, "Which turns out to be the same as the Forward Difference.")


ffer = np.log(ff[0]+1)/np.log(ff[1]+1)
fcer = np.log(fc[0]+1)/np.log(fc[1]+1)

print("Order of Convergence is ", ffer, " for both Forward and Centered Difference.")