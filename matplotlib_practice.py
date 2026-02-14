import matplotlib.pyplot as plt

hours = [1,2,3,4,5]
marks = [40,50,65,80,95]

plt.scatter(hours, marks)
plt.plot(hours, marks)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")
plt.grid(True)
plt.show()
