import math
import matplotlib.pyplot as a


x=[0]
vx=[]
y=[]
vy=[]
z=[0]
vz=[0]
v=[]

y.append(float(raw_input('the initial y coordinate is:')))
v.append(float(raw_input('the initial velocity is:')))
dt=float(raw_input('the time interval is:'))
theta=math.radians(float(raw_input('the firing angel is:')))
vx.append(v[0]*math.cos(theta))
vy.append(v[0]*math.sin(theta))
w=2000/60
sm=0.00041
g=10

i=0
while y[i]>=0:
    xi=x[i]+vx[i]*dt
    bmi=0.0039+0.0058/(1+math.exp((v[i]-35)/5))
    vxi=vx[i]-bmi*v[i]*vx[i]*dt
    yi=y[i]+vy[i]*dt
    vyi=vy[i]-g*dt
    zi=z[i]+vz[i]*dt
    vzi=vz[i]-sm*vx[i]*w*dt
    vi=math.sqrt(vxi**2+vyi**2+vzi**2)
    x.append(xi)
    vx.append(vxi)
    y.append(yi)
    vy.append(vyi)
    z.append(zi)
    vz.append(vzi)
    v.append(vi)
    i+=1

del x[-1]
del y[-1]
del z[-1]

f=a.figure()
p=f.gca(projection='3d')
p.plot(x,z,y)
a.xlabel('x/m')
a.ylabel('y/m')
a.zlabel('z/m')
a.show()