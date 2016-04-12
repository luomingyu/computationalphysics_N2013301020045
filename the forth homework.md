THE FORTH HOMEWORK
======
NO.2013301020045       
NAME：罗明宇     

PURPOSE
------
plot the exercise of chapter 1

Problem
-------
1.4 consider a radioactive decay problem involving two types of nuclei,A and B,with populations NA(t) and NB(t).suppose that type A nuclei decay to form type B nuclei,which then also decay,according to the differential equations     
$$
\frac{dN_A}{dt}=-\frac{N_A}{\tau_A}
$$     
$$
\frac{dN_B}{dt}=\frac{N_A}{\tau_A}-\frac{N_B}{\tau_B}
$$     
Where ta and tb are the decay time constants for each type of nucleus. use the Euler method to solve these coupled equations for NA and NB as functions of time. This problem can also be solved exactly,as was the case with our original nuclear decay problem. Obtain the analytic solutions for NA(t) and NB(t), and compare them with your numerical results, It is also interesting to explore the behavior found for different values of the radio   ta/tb. In particular,try to interpret the short and long time behaviors for different values of this ratio.     
METHOD
--------------
-Input the initialize of this radioactive decay problem,**such** **as** initial number of nuclei A     
-Put the calculation result of every step in the list na and nb     
-Use the matplotlab plot na&nb vs. t     
   like
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/the%20picture%20of%20the%20forth%20homework.png)

code
-----
[the code of the forth homework](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/第四次作业代码.py)
