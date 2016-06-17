import math as ma
from matplotlib import pyplot as plt

class three_bidies:
    def __init__(self,nn):  # nn is growth rate of the mass of Juipter growth rate 
        n_j=1.9/(2000)*nn   # n_j=M_j/M_s
        n_e=6/(2000000)     # n_e=M_e/M_s 
        self.k_j=4*ma.pi**2*n_j
        self.k_e=4*ma.pi**2*n_e   
        self.xe,self.ye=[1],[0]
        self.vex,self.vey=[0],[2*ma.pi]
        self.re=[]
        self.xj,self.yj=[5.2],[0]
        self.vjx,self.vjy=[0],[2*ma.pi/5.2**0.5]
        self.rj=[]        
        self.rej=[]
        self.dt=0.002
        
    def cal(self):
        t=[0]
        while t[-1]<=50:
            rei=ma.sqrt(self.xe[-1]**2+self.ye[-1]**2)
            rji=ma.sqrt(self.xj[-1]**2+self.yj[-1]**2)
            reji=ma.sqrt((self.xe[-1]-self.xj[-1])**2+(self.ye[-1]-self.yj[-1])**2)

            vexi=self.vex[-1]-4*ma.pi**2*self.xe[-1]/rei**3*self.dt-self.k_j*(self.xe[-1]-self.xj[-1])/reji**3*self.dt
            veyi=self.vey[-1]-4*ma.pi**2*self.ye[-1]/rei**3*self.dt-self.k_j*(self.ye[-1]-self.yj[-1])/reji**3*self.dt
            
            vjxi=self.vjx[-1]-4*ma.pi**2*self.xj[-1]/rji**3*self.dt-self.k_e*(self.xj[-1]-self.xe[-1])/reji**3*self.dt
            vjyi=self.vjy[-1]-4*ma.pi**2*self.yj[-1]/rji**3*self.dt-self.k_e*(self.yj[-1]-self.ye[-1])/reji**3*self.dt
            
            xei=self.xe[-1]+vexi*self.dt
            yei=self.ye[-1]+veyi*self.dt
            xji=self.xj[-1]+vjxi*self.dt
            yji=self.yj[-1]+vjyi*self.dt
            
            self.vex.append(vexi)
            self.vey.append(veyi)
            self.vjx.append(vjxi)
            self.vjy.append(vjyi)
            
            self.xe.append(xei)
            self.ye.append(yei)
            self.xj.append(xji)
            self.yj.append(yji)
            
            t.append(t[-1]+self.dt)
            
    def pl(self,style1,slogan1,style2,slogan2):
        plt.plot(self.xe,self.ye,style1,label=slogan1)
        plt.plot(self.xj,self.yj,style2,label=slogan2)
        
  
A=three_bidies(nn=1)
A.cal()
A.pl('b:','Earth','r:','Jupiter')

plt.title('Earth and Jupiter orbiting the Sun with the growth rate 1')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()