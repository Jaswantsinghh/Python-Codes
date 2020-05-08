import numpy as np 
import matplotlib.pyplot as plt 
x=float(input())
y=np.sinh(x) 
in_val = np.linspace(-np.pi, np.pi, 12)
out_val = np.sinh(in_val) 
print("np.sinh (",x,"): ", y)
plt.plot(in_val, out_val, color = 'red', marker = "o")
plt.plot(x,y,color = 'blue', marker = "o")
plt.title("y=sinh(x)") 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.show() 
