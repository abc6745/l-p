import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return (x + 3)**2

def gradient(x):
    return 2 * (x + 3)

x = 2                  
lr = 0.1               
steps = []            

for i in range(20):   
    steps.append(x)
    x = x - lr * gradient(x)

print("Minimum at x =", x)
print("Minimum value y =", f(x))

x = np.linspace(-6, 3, 100)
plt.plot(x, f(x))                   
plt.scatter(steps, f(np.array(steps))) 

plt.title("Gradient Descent")
plt.xlabel("x")
plt.ylabel("y")
plt.show()