**THE FORTH HOMEWORK**
======
NO.2013301020045       
NAME：罗明宇     

**PURPOSE**
------
plot the exercise of chapter 1

**Problem**
-------
1.4 consider a radioactive decay problem involving two types of nuclei,A and B,with populations NA(t) and NB(t).suppose that type A nuclei decay to form type B nuclei,which then also decay,according to the differential equations     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/1.png)     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/2.png)           
Where ta and tb are the decay time constants for each type of nucleus. use the Euler method to solve these coupled equations for NA and NB as functions of time. This problem can also be solved exactly,as was the case with our original nuclear decay problem. Obtain the analytic solutions for NA(t) and NB(t), and compare them with your numerical results, It is also interesting to explore the behavior found for different values of the radio   ta/tb. In particular,try to interpret the short and long time behaviors for different values of this ratio.     
**METHOD**
--------------
- Input the initialize of this radioactive decay problem,**such** **as** initial number of nuclei A     
- Use the Euler approximation to do the calculation,like     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/3.png)     
- Put the calculation result of every step into the list na and nb     
- Use the matplotlab plot na&nb vs. t     
   like     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/4.png)

**code**
-----
[the code of the forth homework](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/4th/第四次作业代码.py)

thanks to [aragornranger/computationalphysics_N2013301020051](https://github.com/aragornranger/computationalphysics_N2013301020051)
