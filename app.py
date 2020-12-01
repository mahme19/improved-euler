import math
import matplotlib
import matplotlib.pyplot as plt

def df(y,t):
    return (y*(1-math.pow(y, 2)))


def funcf(y, t):
    return (math.log(y)-1/2*math.log(y+1)-1/2*math.log(y-1))


stepsize = 1
maxiter = 1000
current_y = -0.000001
lastStepsize = 1
euler_t = 0
current_t = 1
precision = 0.00001
i = 0
t = []
y = []

while(lastStepsize > precision and maxiter > i):
    i = i+1
    previous_y = current_y
    current_y = previous_y+stepsize
    prev_euler_t = euler_t
    euler_t = previous_y + (stepsize * df(previous_y, prev_euler_t))
    previous_t = current_t
    current_t = previous_t + (stepsize * ((df(previous_y, previous_t) + df(current_y, euler_t))/2))
    y.append(current_y)
    t.append(current_t)
    lastStepsize = abs(current_y-previous_y)

plt.plot(t,y)
plt.show()    




                
