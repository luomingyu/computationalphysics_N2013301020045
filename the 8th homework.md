**THE EIGHTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

  Examples of oscillatory phenonmena can be found in many areas of physics, including the motion of electrons in atoms, the behavior of currents and voltages in electronic circuits, and planetary orbits. Perhaps the simplest mechanical system that exhibits such motion is a pendulum, consisting of a mass that is connected by a string to some sort of support so that it is able to swing freely in reponse to the force of gravity.     
  
  
**METHOD**
----

- We consider a simplest model, so we ignore friction and assuming that the angle the string makes with the vertical is small. We used to calculate the model by using Euler method:                   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式1.png)           
- but we find that this solution did not converse energy. Based on the form situation we led to consider other methods of solving ordinary differential equations, like **Runge-Kutta and Verlet methods**. of course, we could change a little of Euler method to be suitable to oscillatory motion like this:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式2.png)           
we call it **Euler-Cromer method**     

**MODEL**
----
- Let us now consider how we might make the simple pendulum a bit realistic. In many cases this damping force is proportional to the velocity, and that is the assumption we will make here. Thus the equation of motion for our damped pendulum has the form:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式3.png)           
where the second term on the right models the friction. Here **q** is a parameter that measures the strength of the damping, and the minus sign guarantees that this force will always oppose the motion of the pendulum. 
The details of solution can be found in many standard mechanics texts, but in short, there are three regimes of distinct physicl behavior. The first regime, is called **underdamped**, occurs for sufficiently small friction, where the solution:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式4.png)           
shows an oscillatory behavior, and an amplitude that decays with time. At the other extreme, when the damoing is large, the behavior is **overdamped**. Here the solution is     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式5.png)           
At the boundary between the underdamped and overdamped regimes, the pendulum is **critically damped** with     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式6.png)           
Numerical results for **theta(t)** in all three cases are shown in following:  
[**code**](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/different%20q.py)        
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/different%20q.png)           
- We therefore consider the addtion of a driving force to the pendulum. The form of this force will depend in how the force is applied. A convenient choice is to assume that the driving force is sinusoidal with time, with amplitude **FD** and angular frequency **omegaD**. This leads to the equation of motion     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式7.png)           
where the last term represents the external driving force.      


**EXERCISE**
----     
- **3.7** Numerically investigate the linear, forced pendulum with friction. Show numerically the existence of the resonance, and conform the dependence of the resonant amplitude on the driving angular frequency **omegaD**, and on the friction parameter **q**.     

[**code**](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/3.7-driven%20pendulum.py)     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/3.7.png)           


- **3.8** In the nonlinear pendulum, use the Euler-Cromer or another suitable method to investigate the relationship between the amplitude and period numerically. Can you give an intuitive argument supporting your results?     

[**code**](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/3.8.py)     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/3.8-1.png)           
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/3.8-2.png)       

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007