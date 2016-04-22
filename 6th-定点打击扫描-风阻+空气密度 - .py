import math
x=[0]
y=[0]
v=[]
vx=[]
vy=[]
vv=[]
g=9.8
th=[]
ex=2.5
ac=0.0065
r=10

xx=float(raw_input("the hitting distance:"))
T=float(raw_input("the temperature of the sea level is(the absolute temperature):"))
bm=float(raw_input("the b/m constant is:"))
vii=float(raw_input("the biggest initial velocity is:"))
v.append(vii)
dt=float(raw_input("the time step:"))
for theta in range(90):
    vx.append(math.cos(math.radians(theta))*v[0])
    vy.append(math.sin(math.radians(theta))*v[0])
    
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
    
    if xx<=x[-2]:
        print "the aimming angel is:",theta,"°"
        break
    else:
        i=1
        while i<len(x):
            del x[i]
            del y[i]
            del v[i]
            i+=1
        vx=[]
        vy=[]

x=[0]
y=[0]        
vx=[]
vy=[]     

for j in range(int(vii)):
    viii=vii-j
    vv.append(viii)
    vx.append(math.cos(math.radians(theta))*vv[0])
    vy.append(math.sin(math.radians(theta))*vv[0])
          
    k=0
    while y[0]>=0:
        xk=x[k]+vx[k]*dt
        vxk=vx[k]-(1-ac*y[k]/T)**ex*bm*vv[k]*vx[k]*dt
        yk=y[k]+vy[k]*dt
        vyk=vy[k]-g*dt-(1-ac*y[k]/T)**ex*bm*vv[k]*vy[k]*dt
        x.append(xk)
        vx.append(vxk)
        y.append(yk)
        vy.append(vyk)
        vvk=math.sqrt(vx[k+1]**2+vy[k+1]**2)
        vv.append(vvk)
        k+=1
        
    if abs(xx-x[-2])<=r:
        break
        print "the aimming velocity is:",j
    else:
        l=1
        while l<len(x):
            del x[l]
            del y[l]
            l+=1
        vv=[]
        vx=[]
        vy=[]
        

