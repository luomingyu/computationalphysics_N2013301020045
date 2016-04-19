import matplotlib.pyplot as a
import math
x=[0]
y=[0]
v=[]
vx=[]
vy=[]
g=9.8
ex=2.5
ac=0.0065

T=float(raw_input("the temperature of the sea level is(the absolute temperature):"))
theta=math.radians(float(raw_input("the angle is:")))
bm=float(raw_input("the b/m constant is:"))
v.append(float(raw_input("the initial velocity is:")))
dt=float(raw_input("the time step:"))
vx.append(math.cos(theta)*v[0])
vy.append(math.sin(theta)*v[0])

i=0
while y[i]>=0:
    xi=x[i]+vx[i]*dt
    vxi=vx[i]-(1-ac*y[i]/T)**ex*bm*v[i]*vx[i]*dt
    yi=y[i]+vy[i]*dt
    vyi=vy[i]-g*dt-(1-ac*y[i]/T)**ex*bm*v[i]*vy[i]*dt
    x.append(xi)
    vx.append(vxi)
    y.append(yi)
    vy.append(vyi)
    vi=math.sqrt(vx[i+1]**2+vy[i+1]**2)
    v.append(vi)
    i+=1

del x[-1]
del y[-1]
print "y=",y[-1]
print "rhe longest distance is:",x[-1]

a.plot(x,y,"b-",label="$50$",linewidth=2)
a.xlabel("x(m)")
a.ylabel("y(m)")
a.grid()
a.title("the trajectory of cannon shell with air drag")
a.legend()
a.show