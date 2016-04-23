import matplotlib.pyplot as a

na=[]
nb=[]
t=[]

na.append(float(raw_input("the initial number of nuclei A:")))
nb.append(float(raw_input("the initial number of nuclei B:")))
tc=float(raw_input("the constant time of nuclei:"))
tt=float(raw_input("the total time:"))
dt=float(raw_input("the time step:"))
t.append(0)

for i in range(int(tt/dt)):
    nai=na[i]+(nb[i]/tc-na[i]/tc)*dt
    nbi=nb[i]+(na[i]/tc-nb[i]/tc)*dt
    ti=t[i]+dt
    na.append(nai)
    nb.append(nbi)
    t.append(ti)
    
a.plot(t,na,"b--",label="$A$",color="red",linewidth=2)
a.plot(t,nb,"b--",label="$B$",color="blue",linewidth=2)
a.xlabel("time(s)")
a.ylabel("the number of the nuclei")
a.grid()
a.title("a radioactive decay problem involving two types of nuclei,A and B")
a.legend()
a.show