import numpy as np
import matplotlib.pyplot as plt
z=np.array([55,60,65,70,75,80,85])
L=np.array([])
eps=np.array([])
L=(7/55)*z
eps=((L-7)*100)/7
print(eps)  
plt.plot(L,eps,color='red', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=3)
# naming the x axis
plt.xlabel('Lenght(cm)')
# naming the y axis
plt.ylabel('strain(%)')
  
# giving a title to my graph
plt.title('Theorical Strain Verus Lenght')
plt.show()

