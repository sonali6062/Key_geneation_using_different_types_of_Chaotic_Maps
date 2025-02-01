#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import matplotlib.pyplot as plt


# In[3]:


dt=0.01
num_steps=10000


# In[4]:


xs=np.empty(num_steps+1)
ys=np.empty(num_steps+1)
zs=np.empty(num_steps+1)


# In[5]:


xs[0],ys[0],zs[0]=(0.1,1,1.05)


# In[6]:


s=10
r=28
b=2.2667
for i in range(num_steps):
    xs[i+1]=xs[i]+(s*(ys[i]-xs[i])*dt)
    ys[i+1]=ys[i]+((xs[i]*(r-zs[i])-ys[i])*dt)
    zs[i+1]=zs[i]+((xs[i]*ys[i]-b*zs[i])*dt)
    


# In[7]:


fig=plt.figure()
ax=fig.gca(projection='3d')
ax.plot(xs,ys,zs,lw=0.5)
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")
ax.set_title("Lorenz Attractor")
plt.show()


# this system is completely deterministic and unpredictable that's why it's chaotic

# # Generating secret keys with chaos: encryption using logistic maps in python

# In[8]:


def keygenerate(x,r,size):
    key=[]
    for i in range(size):
        x=r*x*(1-x)#logistic map
        key.append(int((x*pow(10,16))%256))
    return key
print(keygenerate(0.001,3.9159,10))
    


# In[9]:


print(keygenerate(0.001,3.9145,10))


# WE CAN SEE THAT A MINUTE CHANGE IN CONTOL PARAMETER IS GENERATING A DRASTIC CHANGE IN OUTPUT

# # HENON MAP: discrete-time dynamical system 
# x1=1-a*x*x+y
# 
# y1=b*x
# 
# where, 
# a=1.4, b=0.3

# In[10]:


def Henonmap(x,y,a,b,size):
    x1=y1=0
    for i in range(size):
        x1=1-a*x*x+y
        y1=b*x
        print(x1,"",y1)
        x=x1
        y=y1
Henonmap(0.001,0.2,1.4,0.3,20)


# here 1st column is x-coordinates and 2nd column is y-coordinate

# # ZASLAVSKY MAP
# 
# 
It is a 2-D discrete time dynamical system. It is controlled by 4 parameters μ,ε,τ,ν 


# In[11]:


import math


# In[12]:




def ZaslavskyMap(x, y, r, v, e, size):
    x1 = y1 = 0  # Initial values
    μ = (1 - pow(e, -r)) / r  # μ parameter calculation

    for i in range(size):
        x1 = ((x + v * (1 +μ* y) + e *v* μ * math.cos(2 * math.pi * x)) % 1)
        y1 = pow(e, -r) * (y + e * math.cos(2 * math.pi * x))

        print(x1, "", y1)  # Output x and y values
        x = x1
        y = y1

# Example parameters
v = 4
e = 2.3
r=3
ZaslavskyMap(0.14, 0.13, r, v, e, size=20)


# # BIFURCATION DIAGRAM (r vs x) for logistic map
# x=rx(1-x)

# In[13]:


import matplotlib.pyplot as plt
import numpy as np
R=np.linspace(2.5,4,10000)#control parameter range


# In[14]:


X=[]
Y=[]
for r in R:
    X.append(r)
    x=np.random.random()#initialize x for each r value
    for n in range(100):
        x=r*x*(1-x)
    for n in range(100):
        x=r*x*(1-x)
    Y.append(x)
    
plt.plot(X,Y,ls='',marker=',')
plt.show() 


# In[15]:


R=np.linspace(3.5,4,10000)#for better view
X=[]
Y=[]
for r in R:
    X.append(r)
    x=np.random.random()#initialize x for each r value
    for n in range(100):
        x=r*x*(1-x)
    for n in range(100):
        x=r*x*(1-x)
    Y.append(x)
    
plt.plot(X,Y,ls='',marker=',')
plt.show() 


# In[16]:


R=np.linspace(3.5,4,40000)#for better view
X=[]
Y=[]
for r in R:
    X.append(r)
    x=np.random.random()#initialize x for each r value
    for n in range(100):
        x=r*x*(1-x)
    for n in range(100):
        x=r*x*(1-x)
    Y.append(x)
    
plt.plot(X,Y,ls='',marker=',')
plt.show()


# Can be used for any 1-D graph

# # Lyaponov exponent(ate of separation of infinitely close points)

# Lyapunov exponent(r vs LE)
# Logistic map: r=rx(1-x)

# In[17]:


import matplotlib.pyplot as plt
import numpy as np
R=np.linspace(1,4,20000)#X axis-control parameter range
#specify the total number of points you want in the array, and NumPy will calculate the spacing between the numbers automatically
LE=[]#Y axis-Lyaponov exponent
result=[] 
#Generate x for each value of r
for r in R:
    x=np.random.random()
    for n in range(100):#ignore the
        x=r*x*(1-x)
    result=[]
    for n in range(100):
        x=r*x*(1-x)
        #calculate the log of the absolute of the derivative
        result.append(np.log(abs(r-2*r*x)))
    LE.append(np.mean(result))#average
plt.figure(figsize=(10,7))
plt.grid('on')
plt.plot(R,LE,ls='',marker=',',alpha=1)
plt.show()


# 1st bifurcation is going at r=2, dips shows that its going through bifurcation.
# can be used for any 1-D chaotic map

# # Pseudo random number generator with Zaslavsky map
# 

# 2-D Discrete-time dynnamical system
# 

# In[18]:


import math


# In[19]:


#large application in caotic system related to randomness. can withstand BRUTE-FORCE ATTACK
def ZaslavaskyMap_PRNG(x,y,r,v,e,size):
    prn1=pnr2=pnr3=pnr4=0
    x1=y1=0
    u=(1-pow(e,-r))/r
    for i in range(size):
        x1=((x+v*(1+u*y)+e*v*u*math.cos(2*math.pi*x))%1)#chaotic value
        y1=pow(e,-r)*(y+e*math.cos(2*math.pi*x))
        print("\nChaotic values:",'\nx=',x1,'','\ny=',y1)
        x=x1
        y=y1
        
        #GENERATION of PRNG
        #METHOD1:Extract particular numbers from x1 or y1
        pnr1=x1*10000-math.floor(x1*10000)
        print('\nPNR1=',pnr1)
        
        #METHOD2,3 CONVERT IMAGE IN INTEGER
        #METHOD2:PRN for image encryption using XOR operation of pixel ranges from[0,255]
        pnr2=(math.floor(x1*(math.pow(2,35)-1)))%256
        print('PNR2=',pnr2)
        
        #METHOD3:PRNG for shuffling of pixel values pixel position ranges from[0,len/breadth]
        pnr3=int(math.floor(y1*(math.pow(2,20)-1)))%1024#let size of imzge is 1024
        print('PNR3=',pnr3)
        
        #METHOD4:PNR in binary form
        pnr4=("{0:b}".format(pnr3))
        print('PNR4-Binary form:',pnr4)
x=0.1
y=0.2
v=4#control parameter
e=2.3
r=3
size=2
ZaslavaskyMap_PRNG(x,y,r,v,e,size)


# # BAKER'S MAP

# OBJECTIVE:  Generate chaotic map
# generate keys in the range[0,255]
# generate prime numbers with Baker's map

# In[20]:


from math import sqrt


# In[21]:


import math

def keygen(x, y, a, size):
    key = []
    key1 = []
    xkey = []
    ykey = []

    for i in range(size):
        if 0 <= x <= 0.5:
            x = 2 * x
            y = a * y
        elif 0.5 < x <= 1.0:
            x = 2 * x - 1
            y = a * y + 0.5

        # Append to xkey and ykey instead of x.key and y.key
        xkey.append(x)
        ykey.append(y)

        # Generate encryption keys in range [0, 255]
        key.append(int((x * pow(10, 3)) % 256))
        key1.append(int((x * pow(10, 6)) % 256))

    return xkey, ykey, key, key1

def selectPrime(n):
    primeno = 0  # Flag to check if the number is prime
    p = 0

    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):  # Fix sqrt() usage
            if n % i == 0:
                primeno = 1
                break
        if primeno == 0:
            p = n  # Assign prime number
    return p

if __name__ == "__main__":
    xkey, ykey, key, key1 = keygen(0.18, 0.91, 0.142, 10)

    print('Chaotic values x:', xkey)
    print('Chaotic values y:', ykey)
    print('\nx Key:', key)  # x-value
    print('\ny Key1:', key1)  # y-value

    # Generate prime numbers from this key
    print('\nPrime numbers in x:')
    for i in key:
        p = selectPrime(i)
        if p != 0:
            print(p)

    print('\nPrime numbers in y:')
    for i in key1:
        p = selectPrime(i)
        if p != 0:
            print(p)


# # JSMP MAP

# It is chaotic for a large range 0.502 to 2000
# highly sensitive to even minjte changes in contol parameter and initial conditions.
# It generates a strong encrypted images. leading to high reliability
