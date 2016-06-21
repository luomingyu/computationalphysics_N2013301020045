import numpy as num
import matplotlib.pyplot as plt
import copy as co


'''
class Electric_Field
this class solves the potential euation of capacitor
where: 
              V1: potential of the left plate
              V2: potential of the right palte
              n: size of one side
'''
class ELECTRIC_FIELD(object):
    def __init__(self, V1=1, V2=-1, V_boundary=0, n=30):
        self.V1=float(V1)
        self.V2=float(V2)
        self.V_boundary=float(V_boundary)
        self.n=int(n)
        self.s1, self.s3=int(n/3), int(n/3)
        self.s2, self.s4=int(self.n-2-2*self.s1), int(self.n-2*self.s3)
        self.V=[]
        self.errorc=[]
        self.al=[]
        for j in range(self.n):
            self.V.append([0.0]*self.n)
        for j in range(self.n):
            self.V[j][0]=self.V[j][-1]=self.V_boundary
        for i in range(self.n):
            self.V[0][i]=self.V[-1][i]=self.V_boundary
        for j in range(self.s3,self.s3+self.s4):
            self.V[j][self.s1]=self.V1
            self.V[j][self.s1+self.s2+1]=self.V2    
        self.newV=co.deepcopy(self.V)            
        self.countc=[]    

    def SOR_ALPHA(self): 
        for i in range(5*self.n-10):
            self.alpha=(float(i)+10)/(5*self.n)+1
            self.al.append(self.alpha)
            self.counter=0
            self.V=co.deepcopy(self.newV)
            while True:
                self.delta_V=0.
                for j in range(1,self.n-1):
                    for i in range(1,self.n-1):
                        if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                            continue
                        self.next_V=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                        self.V[j][i]=self.alpha*(self.next_V-self.V[j][i])+self.V[j][i]
                        self.delta_V=self.delta_V+abs(self.alpha*(self.next_V-self.V[j][i]))
                self.counter=self.counter+1
                if self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n:
                    self.countc.append(self.counter)       
                    break
        
        alpha_m_n=self.countc.index(min(self.countc))
        print self.al[alpha_m_n]
  
    def count_relaxation_method(self):
        self.counter=0
        while True:
            self.delta_V=0.
            for j in range(1,self.n-1):
                for i in range(1,self.n-1):
                    if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                        continue
                    self.next_V=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                    self.newV[j][i]=self.next_V
                    self.delta_V=self.delta_V+abs(self.next_V-self.V[j][i])
            self.counter=self.counter+1
            self.V=co.deepcopy(self.newV)
            if self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n:
                print self.counter
                break     
        
    def count_SOR(self):
        self.alpha=2./(1.+num.pi/self.n)
        self.counter=0
        while True:
            self.delta_V=0.
            for j in range(1,self.n-1):
                for i in range(1,self.n-1):
                    if (j in range(self.s3,self.s3+self.s4)) and (i in [self.s1,self.s1+self.s2+1]):
                        continue
                    self.next_V=1./4.*(self.V[j-1][i]+self.V[j+1][i]+self.V[j][i-1]+self.V[j][i+1])
                    self.V[j][i]=self.alpha*(self.next_V-self.V[j][i])+self.V[j][i]
                    self.delta_V=self.delta_V+abs(self.alpha*(self.next_V-self.V[j][i]))
            self.counter=self.counter+1
            if self.delta_V < abs(self.V2-self.V1)*(1.0E-5)*self.n*self.n:
                print self.counter
                break
            
    def pl(self):
        plt.scatter(self.al,self.countc)
        
'''
---------不同alpha计算次数------------
A=ELECTRIC_FIELD()
A.SOR_ALPHA()
A.pl()
plt.xlabel(r'$\alpha$')
plt.ylabel('counter')
plt.title('alpha verse counter')
plt.grid()
plt.legend()
plt.show()

---------取alpha best数据------------
#  为了要避开小于1.1 同时要扩大精度
for i in range(30):
    n_SOR=(i+15)*3
    A=ELECTRIC_FIELD(n_SOR=i+15)
    A.SOR_ALPHA()
    
---------画图---------------
alpha_m_count=[1.46666666667
,1.475
,1.50588235294
,1.51111111111
,1.54736842105
,1.58
,1.57142857143
,1.58181818182
,1.6
,1.61666666667
,1.624
,1.63846153846
,1.65925925926
,1.66428571429
,1.67586206897
,1.68666666667
,1.69677419355
,1.7
,1.71515151515
,1.71764705882
,1.72571428571
,1.73333333333
,1.74054054054
,1.74736842105
,1.75384615385
,1.755
,1.76097560976
,1.76666666667
,1.78139534884
,1.78636363636]
n_SOR=[(i+15)*3 for i in range(30)]
plt.scatter(n_SOR,alpha_m_count)
plt.xlabel('n_SOR')
plt.ylabel(r'$ \alpha$ best')
plt.title('n verse alpha_best')
plt.grid()
plt.show()

---------用不同方法取counter数据-------------
for i in range(30):
    n=(i+15)*3
    A=ELECTRIC_FIELD(n=i+15)
    A.count_relaxation_method()

for i in range(30):
    n=(i+15)*3
    A=ELECTRIC_FIELD(n=i+15)
    A.count_SOR()
 
---------用不同方法画图n-counter数据-------------  
counter_relaxation=[67
,74
,70
,97
,94
,105
,121
,131
,125
,160
,154
,168
,186
,199
,190
,231
,224
,240
,259
,275
,265
,311
,302
,320
,340
,358
,347
,397
,386
,407]
counter_SOR=[23
,25
,27
,28
,30
,32
,33
,35
,37
,38
,39
,41
,42
,44
,46
,47
,48
,50
,51
,53
,55
,56
,57
,59
,60
,62
,64
,64
,66
,68]
for i in range(30):
    n=[(i+15)*3 for i in range(30)]
plt.plot(n,counter_relaxation,'r:',label='relaxation')
plt.plot(n,counter_SOR,'b:',label='SOR')
plt.xlabel('n')
plt.ylabel('counter_relaxation')
plt.title('n verse counter in different method')
plt.grid()
plt.legend()
plt.show()
''' 