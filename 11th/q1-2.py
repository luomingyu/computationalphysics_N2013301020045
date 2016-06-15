import math as ma
from matplotlib import pyplot as plt

class two_bodies:
    def __init__(self,m1m2,x0,vy0):
        # record rhe planet with the mass m1 as the sun
        # r
        self.n=m1m2   # m1m2=m2/m1
        self.x=[x0]
        self.y=[0]
        self.vx=[0]
        self.vy=[vy0]        
        self.dt=0.001

    def trajrctory(self):
        t=[0]
        while t[-1]<=1/ma.sqrt(1+self.n):   
            vxi=self.vx[-1]-4*ma.pi**2*(self.n+1)*self.x[-1]*self.dt
            xi=self.x[-1]+vxi*self.dt
            vyi=self.vy[-1]-4*ma.pi**2*(self.n+1)*self.y[-1]*self.dt
            yi=self.y[-1]+vyi*self.dt
            self.vx.append(vxi)
            self.x.append(xi)
            self.vy.append(vyi)
            self.y.append(yi)
            t.append(t[-1]+self.dt)
            

            
    def pl(self,style,slogan):
        plt.plot(self.x,self.y,style,label=slogan)

   


A=two_bodies(m1m2=2.,x0=-2./3.,vy0=-2*ma.pi*2./ma.sqrt(1+2))
A.trajrctory()
A.pl('b:','m1')

A=two_bodies(m1m2=2.,x0=1./3.,vy0=2*ma.pi/ma.sqrt(1+2))
A.trajrctory()
A.pl('r:','m2')


plt.title('the motion of two_bodies with m2/m1=2 in center-of-mass frame')
plt.xlim(-1,1)
plt.ylim(-1,1)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()