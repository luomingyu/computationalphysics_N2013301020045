import math as ma
from matplotlib import pyplot as plt

class two_bodies:
    def __init__(self,n):
        self.n=n
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[2*ma.pi*ma.sqrt(self.n+1)]
        self.r=[ma.sqrt(self.x[0]**2+self.y[0])]
        self.dt=0.002
        
    def cal(self):
        t=[0]
        while t[-1]<=1:    
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

        
A=two_bodies(n=2)
A.cal()
A.pl('b:','m2')
plt.title('the motion of two_bodies with m2/m1=2 in m1-center frame ')
plt.xlim(-1.5,1.5)
plt.ylim(-1.5,1.5)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()