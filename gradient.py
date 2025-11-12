import matplotlib.pyplot as plt 
def func(x):
	return (x+3)**2
def grad(x):
	return 2*(x+3)
x=2
learning_rate=0.1
epochs=50
tolerance=1e-4
x_vals=[x]
y_vals=[func(x)]
for i in range(epochs):
	dx=grad(x)
	x_new=x-learning_rate*dx
	if abs(x_new-x)<tolerance:
		x=x_new
		print(f"Iteration {i+1}: x = {x:.5f}, f(x) = {func(x):.5f}")
		print(f"Stopped early at Iteration {i+1} at x = {x:.5f}, f(x) = {func(x):.5f}")
		break
	x=x_new
	x_vals.append(x)
	y_vals.append(func(x))
	print(f"Iteration {i+1}: x = {x:.5f}, f(x) = {func(x):.5f}")
print(f"Local minima at x = {x:.5f}, f(x) = {func(x):.5f}")

plt.figure(figsize=(14,8))
x_plot=[i for i in range(-10,5)]
y_plot=[func(i) for i in x_plot]
plt.plot(x_plot,y_plot,label="(x+3)**2", color='blue')
plt.scatter(x_vals,y_vals,label="Gradient Descent Steps", color='red')
plt.plot(x_vals,y_vals,color='gray',alpha=0.8)
plt.title("Gradient Descent to find Local Minima")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.legend()
plt.show()