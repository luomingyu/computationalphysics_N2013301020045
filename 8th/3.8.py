import math
import matplotlib.pyplot as plt

g=9.8

class driven_pendulum:
    def __init__(self,alpha=30,l=1,t_end=0.1,dt=0.001):
        self.theta0=math.radians(alpha)
        self.l=l
        self.omega0=0
        self.theta=[self.theta0]
        self.omega=[self.omega0]
        self.t_end=t_end
        self.dt=dt
        self.t=[0]
        
    def trajectory(self):
        for i in range(int(self.t_end/self.dt)):
            omegai=self.omega[i]-g/self.l*math.sin(self.theta[i])
            thetai=self.theta[i]+omegai*self.dt
            ti=(i+1)*self.dt
            self.omega.append(omegai)
            self.theta.append(thetai)
            self.t.append(ti)

    def pl(self,style='',slogan=''):
            plt.plot(self.t,self.theta,style,label=slogan)
        
A=driven_pendulum(alpha=30)
A.trajectory()
A.pl(style='r-',slogan='alpha=30')

B=driven_pendulum(alpha=35)
B.trajectory()
B.pl(style='b--',slogan='alpha=35')

C=driven_pendulum(alpha=40)
C.trajectory()
C.pl(style='g-.',slogan='alpha=40')

D=driven_pendulum(alpha=45)
D.trajectory()
D.pl(style='k-,',slogan='alpha=45')

plt.xlabel('Time(s)')
plt.ylabel('theta(rad)')
plt.grid()
plt.title('theta & t with different initial angel')
plt.legend()
plt.show()