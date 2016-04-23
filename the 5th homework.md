**THE FIFTH HOMEWORK**
======
NO.2013301020045       
NAME：罗明宇     

**PURPOSE**
------
plot the exercise of chapter 1

**Problem**
-------
1.5 consider again a decay problem with two types of nuclei,A and B , but now suppose that nuclei of type A decay into ones of type B , while nuclei of type B decay into ones of type A . Strictly speaking , this is not a "decay" process , since it is possible for the type B nuclei to turn back into type A nuclei . A better analogy would be a resonance in which a system can tunnel or move back and forth between two states A and B which have equal energies . The corresponding rate equations are       
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/5th/1.png)     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/5th/2.png)      
Where for simplicity we have assumed that the two types of decay are charaterized by the same time constant . Solve this system of equations for the numbers of nuclei, NA and NB , as functions of time .  Consider different initial conditions . Show that steady  state in which NA and NB are constant . In such a steady state , the time derivatives dNA/dt and dNB/dt should vanish .         


**METHOD**
--------------
-Input the initialize of this radioactive decay problem,**such** **as** initial number of nuclei A     
-Use the Euler approximation to do the calculation,like     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/3.png)     
-Put the calculation result of every step into the list na and nb     
-Use the matplotlab plot na&nb vs. t     
   like
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/5th/3.png)      


**code**
-----
[the code of the fifth homework](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/5th/第五次作业代码.py)

thanks to [aragornranger/computationalphysics_N2013301020051](https://github.com/aragornranger/computationalphysics_N2013301020051)
