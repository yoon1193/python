import matplotlib.pyplot as plt
import numpy as np

# x_data = np.random.rand(100)
# y_data = np.random.rand(100)

# plt.title('scatter plot')
# plt.grid()
# plt.scatter(x_data,y_data,color='b',marker='o')
# plt.show()

x_data = [x for x in range(-5,5)]
y_data = [y*y for y in range(-5,5)]
x_data = [-3,-2,-1,0,1,2,3]
y_data = [3,2,1,10,11,12,13]
plt.title('line')
plt.grid()
plt.plot(x_data,y_data,color='g')
plt.show()