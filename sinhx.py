import numpy as np 
import matplotlib.pyplot as plt 
x=float(input())
y=np.sinh(x) 
print("sinh (",x,"): ", y)
in_val = []
for i in range(1,int(x+10),2):
    in_val.append(-np.pi/i)
in_val.append(0)
in_val.append(x)
for i in range(1,int(x+10),2):
    in_val.append(np.pi/i)
in_val=sorted(in_val)
out_val=np.sinh(in_val)
plt.plot(in_val, out_val, color = 'red', marker = "o",)
plt.plot(x,y,color = 'blue', marker = "o")
plt.annotate("(0,0)", (-0.5, 0.7))
plt.axis([int(x)-10, int(x)+10, int(y)-30, int(y)+10])
plt.title("y=sinh(x)") 
plt.hlines(y=0, xmin=int(x)-10, xmax=0)
plt.vlines(x=0, ymin=int(y)-30, ymax=0)
plt.xlabel("X") 
plt.ylabel("Y")
plt.grid()
plt.show() 
