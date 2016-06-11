import math
import matplotlib.pyplot as plt

g=9.8
l=9.8

class chaoic:
    def __init__(self,Fd=1.2,omegad=2./3,t_end=1000):
        self.theta0=0.2
        self.q=0.5
        self.omega0=0
        self.omegad=omegad
        self.step=100
        self.cycle=2*math.pi/self.omegad
        self.dt=self.cycle/self.step
        self.omegad=2./3
        self.theta=[self.theta0]
        self.omega=[self.omega0]
        self.Fd=Fd
        self.t=[0]
        self.t_end=t_end
    def phase(self):
        while self.t[-1]<=self.t_end:
            omegai=self.omega[-1]+(-math.sin(self.theta[-1])-self.q*self.omega[-1]+self.Fd*math.sin(self.omegad*self.t[-1]))*self.dt
            self.omega.append(omegai)
            thetai=self.theta[-1]+omegai*self.dt
            if thetai>math.pi:
                thetai-=2*math.pi
            if thetai<-math.pi:
                thetai+=2*math.pi
            self.theta.append(thetai)
            ti=self.t[-1]+self.dt
            self.t.append(ti)
            
    def out_phase(self,ini,color,slogan):
        self.n=int(self.t_end//self.cycle)
        self.new_omega=[]
        self.new_theta=[]
        for i in range(self.n):
            self.xxx=int((i+ini)*self.step)
            self.new_omega.append(self.omega[self.xxx])
            self.new_theta.append(self.theta[self.xxx])
        plt.scatter(self.new_theta,self.new_omega,s=0.5,c=color,label=slogan)

    def pl(self,style,slogan):
        plt.plot(self.t,self.omega,style,label=slogan)
     

#     
A=chaoic(Fd=2,t_end=50)
A.phase()
A.pl('r-','Fd=0.5')
plt.subplot(111)
plt.xlabel(r'$\theta$ [rad]')
plt.ylabel(r'$\omega$ [$s^{-1}$]')
plt.legend()
plt.show()  
     
A=chaoic(Fd=1.2,omegad=3./4,t_end=5000)
A.phase()
plt.subplot(221)
A.out_phase(ini=0,color='b',slogan=r'$t\approx 2\pi n/\Omega_D$')
plt.xlabel('$\omega$(rad)')
plt.ylabel('$\theta$(rad)')
plt.grid()
plt.legend()

plt.subplot(222)
A.out_phase(ini=0.25,color='b',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/4$')
plt.xlabel('$\omega$(rad)')
plt.ylabel('$\theta$(rad)')
plt.grid()
plt.legend()

plt.subplot(223)
A.out_phase(ini=0.5,color='b',slogan=r'$t\approx 2\pi n/\Omega_D+\pi/2$')
plt.xlabel('$\omega$(rad)')
plt.ylabel('$\theta$(rad)')
plt.grid()
plt.legend()

plt.subplot(224)
A.out_phase(ini=0.75,color='b',slogan=r'$t\approx 2\pi n/\Omega_D+3\pi /4$')
plt.xlabel('$\omega$(rad)')
plt.ylabel('$\theta$(rad)')
plt.grid()
plt.legend()

plt.show()

