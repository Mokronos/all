import time
import numpy as np
import matplotlib.pyplot as plt
import random
x = np.array([[0,0]])
a = np.array([[1,0.71],[0,0.71]])
b = np.array([[0,0],[0,1]])
y = np.matmul(a,b,np.linalg.inv(a))
z = np.matmul(y,np.array([1,0]))
plt.ion()
fig, ax = plt.subplots()
sc = ax.scatter(x[:,0],x[:,1])
x1, y1 = [0,0], [0,0]
test = ax.plot(x1, y1)

plt.xlim(-40,40)
plt.ylim(-40,40)
plt.draw()
plt.grid()
print(x)
for i in range(100):
    #scatter(x[:,0],x[:,1])
    #plt.draw()

    #plt.close()
    c=random.randint(1,4)
    if c==1:
        x[:,0]=x[:,0]+1
    elif c==2:
        x[:,0]=x[:,0]-1
    elif c==3:
        x[:,1]=x[:,1]+1
    elif c==4:
        x[:,1]=x[:,1]-1
    time.sleep(.000001)
    #test = ax.plot([0,x[:,0]],[0,x[:,1]])
    #sc.set_offsets(x)
    ax.clear()
    ax.scatter(x[:,0],x[:,1])
    ax.plot([0,x[:,0]],[0,x[:,1]])
    plt.xlim(-40,40)
    plt.ylim(-40,40)
    plt.draw()
    fig.canvas.draw_idle()
    plt.pause(0.1)

plt.waitforbuttonpress()
