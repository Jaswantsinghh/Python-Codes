import numpy as np 
import matplotlib.pyplot as plt 
x=float(input())
y=np.sinh(x) 
print("np.sinh (",x,"): ", y)
in_val = []

in_val.append(-np.pi)
in_val.append(-np.pi/2)
in_val.append(-np.pi/3)
in_val.append(-np.pi/6)
in_val.append(0)
in_val.append(np.pi/6)
in_val.append(x)
in_val.append(np.pi/3)
in_val.append(np.pi/2)
in_val.append(np.pi)

in_val=sorted(in_val)
out_val=np.sinh(in_val)

 
plt.plot(in_val, out_val, color = 'red', marker = "o")
plt.plot(x,y,color = 'blue', marker = "o")
plt.title("y=sinh(x)") 
plt.xlabel("X") 
plt.ylabel("Y") 
plt.show() 
