import math
import matplotlib.pyplot as plt

g=9.8

class driven_pendulum:
    def __init__(self,alpha=30,q=1,l=1,t_end=10,dt=0.0001,omegad=2,F=0.2):
        self.theta0=math.radians(alpha)
        self.q=q
        self.l=l
        self.omega0=0
        self.theta=[self.theta0]
        self.omega=[self.omega0]
        self.t_end=t_end
        self.dt=dt
        self.t=[0]
        self.omegad=omegad
        self.F=F
        
    def trajectory(self):
        for i in range(int(self.t_end/self.dt)):
            omegai=self.omega[i]-g/self.l*self.theta[i]*self.dt-self.q*self.omega[i]*self.dt+self.F*math.sin(self.omegad*self.t[i])*self.dt
            thetai=self.theta[i]+omegai*self.dt
            ti=(i+1)*self.dt
            self.omega.append(omegai)
            self.theta.append(thetai)
            self.t.append(ti)

    def pl(self,style='',slogan=''):
            plt.plot(self.t,self.theta,style,label=slogan)
        
A=driven_pendulum(omegad=2,F=0.2)
A.trajectory()
A.pl(style='r-',slogan='omegad=2,F=0.2')

B=driven_pendulum(omegad=2,F=0.4)
B.trajectory()
B.pl(style='b--',slogan='omegad=2,F=0.4')

C=driven_pendulum(omegad=4,F=0.2)
C.trajectory()
C.pl(style='g-.',slogan='omegad=4,F=0.2')

D=driven_pendulum(omegad=4,F=0.4)
D.trajectory()
D.pl(style='k-,',slogan='omegad=4,F=0.4')

plt.xlabel('Time(s)')
plt.ylabel('theta(rad)')
plt.grid()
plt.title('theta & t with different q')
plt.legend()
plt.show()