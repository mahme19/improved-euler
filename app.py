import matplotlib
import matplotlib.pyplot as plt

def f(y):
    return (y*(1-pow(y,2)))


h = 0.05
maxiter = 1000000
lastStepsize = 1
current_y = -0.1 
current_t = 0 
precision = 0.000001  
i = 0
t = []
y = []

while(maxiter > i):
    i = i+1
    previous_t = current_t
    current_t = previous_t + h 
    previous_y = current_y
    current_y = previous_y + h * ((f(previous_y) + f(previous_y + h * f(previous_y)))/2)
    y.append(current_y)
    t.append(current_t)
    lastStepsize = abs(previous_t - current_t)

print(current_y)
print(current_t)
print(i)

plt.plot(t,y)
plt.show()

                
