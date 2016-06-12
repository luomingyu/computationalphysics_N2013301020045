from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt


class lorenz_model:
    def __init__(self,tau=5):
        self.sigma=10
        self.b=8./3
        self.tau=tau
        self.dt=0.0001
        self.x=[1]
        self.y=[0]
        self.z=[0]
        self.t=[0]
        self.t_end=50
        
    def Euler_method(self):
        while self.t[-1]<=self.t_end:
            self.xi=self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt
            self.yi=self.y[-1]+(-self.x[-1]*self.z[-1]+self.tau*self.x[-1]-self.y[-1])*self.dt
            self.zi=self.z[-1]+(self.x[-1]*self.y[-1]-self.b*self.z[-1])*self.dt
            self.x.append(self.xi)
            self.y.append(self.yi)
            self.z.append(self.zi)
            self.t.append(self.t[-1]+self.dt)

        
    def phase_section(self):
        self.dt=0.0001
        self.new_y_x0=[]
        self.new_z_x0=[]
        self.new_z_y0=[]
        self.new_x_y0=[]
        while self.t[-1]<=1000:
            self.xi=self.x[-1]+self.sigma*(self.y[-1]-self.x[-1])*self.dt
            self.yi=self.y[-1]+(-self.x[-1]*self.z[-1]+self.tau*self.x[-1]-self.y[-1])*self.dt
            self.zi=self.z[-1]+(self.x[-1]*self.y[-1]-self.b*self.z[-1])*self.dt
            self.x.append(self.xi)
            self.y.append(self.yi)
            self.z.append(self.zi)
            self.t.append(self.t[-1]+self.dt)

            if self.t[-1]>30:
                if abs(self.xi)<=0.001:
                    self.new_y_x0.append(self.yi)
                    self.new_z_x0.append(self.zi)
                if abs(self.yi)<=0.001:
                    self.new_x_y0.append(self.xi)
                    self.new_z_y0.append(self.zi)

        
    def pltz(self,style,slogan):
        plt.plot(self.t,self.z,style,label=slogan)
        plt.title('Lorenz model z verse time')
        plt.xlabel('time')
        plt.ylabel('z')
        
    def plxz(self,style):
        plt.plot(self.x,self.z,style)
        plt.xlabel('x')
        plt.ylabel('z')
        
    def pl3d(self):
        f=plt.figure()
        p=f.gca(projection='3d')
        p.plot(self.x,self.y,self.z)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()
    
    def pl_section_yz(self,color,slogan):
        plt.scatter(self.new_y_x0,self.new_z_x0,s=0.1,c=color,label=slogan)
        plt.title('Phase space plot: z verse y when x=0')
        plt.xlabel('y')
        plt.ylabel('z')
        plt.legend()
        plt.show()

    def pl_section_xz(self,color,slogan):
        plt.scatter(self.new_x_y0,self.new_z_y0,s=0.1,c=color,label=slogan)
        plt.title('Phase space plot: z verse x when y=0')
        plt.xlabel('x')
        plt.ylabel('z')
        plt.legend()
        plt.show()


#picture 1：   
#A=lorenz_model(tau=5)
#A.Euler_method()
#A.pltz('r--','r=5')

#B=lorenz_model(tau=10)
#B.Euler_method()
#B.pltz('b:','r=10')

#C=lorenz_model(tau=25)
#C.Euler_method()
#C.pltz('k-','r=25')

#plt.legend()
#plt.show()


#picture 2:
#A=lorenz_model(tau=25)
#A.Euler_method()
#A.plxz('k-')

#plt.title('Phase space plot z verse x')

#plt.legend()
#plt.show()


#pictyre 2+:
#A=lorenz_model(tau=25)
#A.Euler_method()
#A.pl3d()


#picture 3-1:
#A=lorenz_model(tau=25)
#A.phase_section()
#A.pl_section_yz(color='b',slogan='r=25')


#picture 3-2:
#A=lorenz_model(tau=25)
#A.phase_section()
#A.pl_section_xz(color='b',slogan='r=25')

