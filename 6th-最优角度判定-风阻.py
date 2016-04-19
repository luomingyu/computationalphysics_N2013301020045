import math
x=[0]
y=[0]
v=[]
vx=[]
vy=[]
g=9.8
L=[]
th=[]

bm=float(raw_input("the b/m constant is:"))
v.append(float(raw_input("the initial velocity is:")))
dt=float(raw_input("the time step:"))
for theta in range(90):
    vx.append(math.cos(math.radians(theta))*v[0])
    vy.append(math.sin(math.radians(theta))*v[0])
    th.append(theta)
    i=0
    while y[i]>=0:
        xi=x[i]+vx[i]*dt
        vxi=vx[i]-bm*v[i]*vx[i]*dt
        yi=y[i]+vy[i]*dt
        vyi=vy[i]-g*dt-bm*v[i]*vy[i]*dt
        x.append(xi)
        vx.append(vxi)
        y.append(yi)
        vy.append(vyi)
        vi=math.sqrt(vx[i+1]**2+vy[i+1]**2)
        v.append(vi)
        i+=1
        
    L.append(x[-2])
    i=1
    while i<len(x):
        del x[i]
        del y[i]
        del v[i]
        i+=1
    vx=[]
    vy=[]

md=max(L)
nu=L.index(md)
print "the best angel is:",nu
print "the corresponding distance is:",md