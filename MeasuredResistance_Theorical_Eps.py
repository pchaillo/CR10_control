import numpy as np
import matplotlib.pyplot as plt
z=np.array([55,60,65,70,75,80,85])
L=np.array([])
eps=np.array([])
L=(7/55)*z
eps=((L-7)*100)/7
Ru=np.array([1.77,1.9,2.2,2.25,2.11,2.06,2.35])
Rd=np.array([1.87,1.93,2,2.11,2.27,2.5,2.4])
print(eps)  
plt.plot(eps,Ru,color='red', linewidth = 1,
         marker='o', markerfacecolor='blue', markersize=3,label="traction")
plt.plot(eps,Rd,color='blue', linewidth = 1,
         marker='o', markerfacecolor='red', markersize=3,label="compression")         
# naming the x axis
plt.xlabel('strain(%)')
# naming the y axis
plt.ylabel('Resistance(kohm)')
  
# giving a title to my graph
plt.title('Resistance Verus strain')
plt.show()

