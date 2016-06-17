import math as ma
from matplotlib import pyplot as plt

class three_bidies:
    def __init__(self,nn,theta_e=0,theta_j=0):  
    # nn is growth rate of the mass of Juipter growth rate 
    # the x,y cooridinate is relative to the Sun
        n_j=1.9/(2000)*nn   # n_j=M_j/M_s
        n_e=6/(2000000)     # n_e=M_e/M_s
        self.k_j=4*ma.pi**2*n_j   
        self.k_e=4*ma.pi**2*n_e
        self.k_s=4*ma.pi**2
        
        theta_e=ma.radians(theta_e)
        theta_j=ma.radians(theta_j)
        
        r_e,r_j=1,5.2
        x_e0,y_e0=r_e*ma.cos(theta_e),r_e*ma.sin(theta_e)
        x_j0,y_j0=r_j*ma.cos(theta_j),r_e*ma.sin(theta_j)
        
        x_center=(n_j*x_j0+n_e*x_e0)/(1+n_j+n_e)
        y_center=(n_j*y_j0+n_e*y_e0)/(1+n_j+n_e)

        self.xe,self.ye=[x_e0-x_center],[y_e0-y_center]
        self.vex,self.vey=[2*ma.pi*ma.sin(theta_e)],[2*ma.pi*ma.cos(theta_e)]
        
        self.xj,self.yj=[x_j0-x_center],[y_j0-y_center]
        self.vjx,self.vjy=[2*ma.pi/5.2**0.5*ma.sin(theta_j)],[2*ma.pi/5.2**0.5*ma.cos(theta_j)]
        
        self.xs,self.ys=[-x_center],[-y_center]
        self.vsx,self.vsy=[-2*ma.pi*ma.sin(theta_e)*n_e-2*ma.pi/5.2**0.5*ma.sin(theta_j)*n_j],[-2*ma.pi*ma.cos(theta_e)*n_e-2*ma.pi/5.2**0.5*ma.cos(theta_j)*n_j]
        
        self.res=[]
        self.rjs=[] 
        self.rej=[]
        
        self.dt=0.002
        
    def cal(self):
        t=[0]
        while t[-1]<=100:
            resi=((self.xs[-1]-self.xe[-1])**2+(self.ys[-1]-self.ye[-1])**2)**0.5
            rjsi=((self.xs[-1]-self.xj[-1])**2+(self.ys[-1]-self.yj[-1])**2)**0.5
            reji=((self.xe[-1]-self.xj[-1])**2+(self.ye[-1]-self.yj[-1])**2)**0.5

            vexi=self.vex[-1]-self.k_s*(self.xe[-1]-self.xs[-1])/resi**3*self.dt-self.k_j*(self.xe[-1]-self.xj[-1])/reji**3*self.dt
            veyi=self.vey[-1]-self.k_s*(self.ye[-1]-self.ys[-1])/resi**3*self.dt-self.k_j*(self.ye[-1]-self.yj[-1])/reji**3*self.dt
            
            vjxi=self.vjx[-1]-self.k_s*(self.xj[-1]-self.xs[-1])/rjsi**3*self.dt-self.k_e*(self.xj[-1]-self.xe[-1])/reji**3*self.dt
            vjyi=self.vjy[-1]-self.k_s*(self.yj[-1]-self.ys[-1])/rjsi**3*self.dt-self.k_e*(self.yj[-1]-self.ye[-1])/reji**3*self.dt
            
            vsxi=self.vsx[-1]-self.k_j*(self.xs[-1]-self.xj[-1])/rjsi**3*self.dt-self.k_e*(self.xs[-1]-self.xe[-1])/resi**3*self.dt
            vsyi=self.vsy[-1]-self.k_j*(self.ys[-1]-self.yj[-1])/rjsi**3*self.dt-self.k_e*(self.ys[-1]-self.ye[-1])/resi**3*self.dt            
            
            xei=self.xe[-1]+vexi*self.dt
            yei=self.ye[-1]+veyi*self.dt
            xji=self.xj[-1]+vjxi*self.dt
            yji=self.yj[-1]+vjyi*self.dt
            xsi=self.xs[-1]+vsxi*self.dt
            ysi=self.ys[-1]+vsyi*self.dt
            
            self.vex.append(vexi)
            self.vey.append(veyi)
            self.vjx.append(vjxi)
            self.vjy.append(vjyi)
            self.vsx.append(vsxi)
            self.vsy.append(vsyi)
            
            self.xe.append(xei)
            self.ye.append(yei)
            self.xj.append(xji)
            self.yj.append(yji)
            self.xs.append(xsi)
            self.ys.append(ysi)
            
            t.append(t[-1]+self.dt)
            
    def pl(self,style1,slogan1,style2,slogan2,style3,slogan3):
        plt.plot(self.xe,self.ye,style1,label=slogan1)
        plt.plot(self.xj,self.yj,style2,label=slogan2)
        plt.plot(self.xs,self.ys,style3,label=slogan3)

    def pl_d(self):
        plt.plot(self.xe,self.ye)
        plt.plot(self.xj,self.yj)
        plt.plot(self.xs,self.ys)
'''
A=three_bidies(nn=1)
A.cal()
A.pl('b:','Earth','r:','Jupiter','k-','Sun')
plt.title('Earth and Jupiter orbiting the Sun with the growth rate 1')
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()
plt.legend()
plt.show()
'''
'''
#-----------木星质量增长变化 ------------------
B=three_bidies(nn=1)
B.cal()
plt.subplot(221)
B.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

C=three_bidies(nn=10)
C.cal()
plt.subplot(222)
C.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()


D=three_bidies(nn=100)
D.cal()
plt.subplot(223)
D.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()


E=three_bidies(nn=1000)
E.cal()
plt.subplot(224)
E.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()
'''
'''
#-----------角度变化 0-90 ------------------
F=three_bidies(nn=100,theta_e=0)
F.cal()
plt.subplot(221)
F.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

G=three_bidies(nn=100,theta_e=30)
G.cal()
plt.subplot(222)
G.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

H=three_bidies(nn=100,theta_e=60)
H.cal()
plt.subplot(223)
H.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

I=three_bidies(nn=100,theta_e=90)
I.cal()
plt.subplot(224)
I.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()
'''
'''
#-----------角度变化 120-180 ------------------
J=three_bidies(nn=100,theta_e=120)
J.cal()
plt.subplot(221)
J.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

K=three_bidies(nn=100,theta_e=150)
K.cal()
plt.subplot(222)
K.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

L=three_bidies(nn=100,theta_e=180)
L.cal()
plt.subplot(223)
L.pl_d()
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()
'''

#-----------角度变化 0-90 ------------------
F=three_bidies(nn=1000,theta_e=0)
F.cal()
plt.subplot(221)
F.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

G=three_bidies(nn=1000,theta_e=30)
G.cal()
plt.subplot(222)
G.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

H=three_bidies(nn=1000,theta_e=60)
H.cal()
plt.subplot(223)
H.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

I=three_bidies(nn=1000,theta_e=90)
I.cal()
plt.subplot(224)
I.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()

'''
#-----------角度变化 120-180 ------------------
J=three_bidies(nn=1000,theta_e=120)
J.cal()
plt.subplot(221)
J.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

K=three_bidies(nn=1000,theta_e=150)
K.cal()
plt.subplot(222)
K.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

L=three_bidies(nn=1000,theta_e=180)
L.cal()
plt.subplot(223)
L.pl_d()
plt.xlim(-10,10)
plt.ylim(-10,10)
plt.xlabel('x(AU)')
plt.ylabel('y(AU)')
plt.grid()

plt.show()
'''