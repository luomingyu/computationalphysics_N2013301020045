import math as ma
from matplotlib import pyplot as plt

class solar_system:
    def __init__(self):
        self.x=[1]
        self.y=[0]
        self.vx=[0]
        self.vy=[2*ma.pi]
        self.r=[ma.sqrt(self.x[0]**2+self.y[0])]
        self.dt=0.002
        
    def cal(self):
        t=[0]
        while t[-1]<=1:    
            vxi=self.vx[-1]-4*ma.pi**2*self.x[-1]/self.r[-1]**3*self.dt
            xi=self.x[-1]+vxi*self.dt
            vyi=self.vy[-1]-4*ma.pi**2*self.y[-1]/self.r[-1]**3*self.dt
            yi=self.y[-1]+vyi*self.dt
            ri=ma.sqrt(xi**2+yi**2)
            self.vx.append(vxi)
            self.x.append(xi)
            self.vy.append(vyi)
            self.y.append(yi)
            self.r.append(ri)
            t.append(t[-1]+self.dt)
            
    def pl(self,style,slogan):
        plt.plot(self.x,self.y,style,label=slogan)
        plt.title('Earth orbiting the Sun')
        plt.xlim(-1.5,1.5)
        plt.ylim(-1.5,1.5)
        plt.xlabel('x(AU)')
        plt.ylabel('y(AU)')
        plt.grid()
        plt.legend()
        plt.show()
        
A=solar_system()
A.cal()
A.pl('b:','earth')
