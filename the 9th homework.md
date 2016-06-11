**THE NINTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

We now generalize our pendulum model to include the effects of friction and nonlinear and find that they give rise to the possibiblity of chaoic behavior. While the term chaos probably has some intuitive meaning for all of us, it is not easy to give a precise definition of this notion.     
  
  
**METHOD**
----

- We consider a simplest model, so we ignore friction and assuming that the angle the string makes with the vertical is small. We used to calculate the model by using Euler method:                   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式1.png)           
- but we find that this solution did not converse energy. Based on the form situation we led to consider other methods of solving ordinary differential equations, like **Runge-Kutta and Verlet methods**. of course, we could change a little of Euler method to be suitable to oscillatory motion like this:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/8th/公式2.png)           
we call it **Euler-Cromer method**     

**MODEL**
----
- Now that we have a numerical method that is suitable for various versions of the simple pendulum problem, and armed with some understanding of what might or might not happen when dissipation, an external driving force, and/or nonlinearity is present, we are ready to take on a slightly more complicated and also more interesting sitution. That is, we add all three ingredients which were previously only discussed separately. First, we do not assume the small-angle approximation, and thus do not expand **sin(theta)** term. Second, we include friction of the form **-q(d(theta)/dt)**. Third, we add to our model a sinusoidal driving force **F_Dsin(omega_D*t)**. Putting all of these ingredients together, we have the equation of motion        
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/公式1.png)           
 so we can use the Euler-Cromer method to have the following equation      
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/公式2.png)         
- There are several differences of note. First, the equation for **omega_i+1** is more complicated since we have a different equation of motion. Second, we adjust the value of **theta** after each iteration so as to keep it always between **-pi** and **pi**. Recall that our pendulum can now swing all the way around its pivot point, which corresponds to **|theta|>pi**. Finally, note that we again use the Euler-Cromer method, but the Runge-Kutta or Verlet methods would also be suitable.          
- The behavior changes radically when the driving force is increased to **F_D=1.2**. Now the motion is no longer simple, even at long time. For this value of the driving force the behavior never repeats. This is an example of **chaoic** behavior, which will be our main concern for the rest of this chapter.
- It is important to appreciate the behavior illustrated in following     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D0.png)         
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D0.5.png)         
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D1.2.png)         
At low drive the motion is a simple oscillation, which would, if we were sufficiently patient, repeat forever. One the other hand, at high drive the motion is chaoic; it is a very complicated nonrepeating function of time.Its behavior id random and unpredictable. Our system is thus both deterministic and unpredictable. Put another way, a system can obey certain deterministic laews of physics, but still exhibit behavior that is unpredictable due to an extreme sensitivity to initial conditions. This is what it means to be **chaoic**.     
- However, it turns out that this view is too pessimistic. It is possible to make certain accurate predictions concerning **theta**, even in the chaoic regime! To demonstrate this we need to consider the trajectory in a different way. Instead of plotting **theta** as a function of **t**, let us plot the angular velocity **omega** as a function of **theta**. This is sometimes referred to as a **phase-space** plot. Since we have already constructed a program to calculate **theta** and **omega**, it is straightforward to modify it to make the desired plot; reaults for two values of the drive amplitude are shown in following      
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/混沌Fd%3D0.5.png)         
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/混沌Fd%3D1.2.png)         
- With a small driving force the trajrctory in phase-space(**omega-theta** space) is easy to understand in terms of the behavior we found earlier for **theta(t)**. For short times there is a transient that depends on the initial conditions ( in this case we started at **theta=0.2** with **omega=0** ), but the pendulum quickly settles into a regular orbit in phase space corresponding to the oscillatory motion of motion of both **theta** and **omega**. It can be shown that this final orbit is indeprndent of the initial conditions; this is also what our results for the Lyapunov exponent imply. The behavior in the chaotic regime is a bit more surprising. The phase-space trajectory exhibits many orbits that are nearly closed and that persist for only one or two cycles. While this pattern is certainly not a simple one, it is not completely random, as might have been expected for a chaoic system. This is a common property of chaoic system.     
- If we examine these trajectories in a slightly different manner we find a very striking result. In the following picture we show the same type of phase-space graph, but here we plot **omega** verse **theta** only at times that are in phase with the driving force. That is, we only display the point when **omega_D*t=2n*pi**, where **n** is an integer. This is an example of what is known as a **Poincare section** and is a very useful way to plot and analyze the behavior of a dynamical system. The motivation for plotting the results in this way can be appreciated from an analogy with the function of a stroboscope.        

 

**EXERCISE**
----
[**code**](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/chaoic.py)          
--
- **3.12** In constructing the **Poincare section** we plotted points only at times that were in phase with the drive force; that is, at times **t=2pi*n/omega_D**, where **n** is an integer. At these values of **t** the driving force passed through zero. However, we could just as easily have chosen to make the plot at times correponding to a maximum of the drive force, or at times **pi/4** out-of-phase with this force, ect. Construct the **Poincare section** for these cases and compare them.     

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D1.2，OMEGAD%3D0.66667.png)           


- **3.16** Investigate how a strange attractor is altered by small changes in one of the pendulum parameters. Begin by calculating the strange attractor. Then change either the drive amplitude or drive frequency by a small amount and observe the changes in the attrator.    

F_D=1.2，OMEGA_D=0.66667     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D1.2，OMEGAD%3D0.66667.png)        

F_D=1.2，OMEGA_D=0.75     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D1.2%2Comega%3D0.75.png)        

F_D=1.1，OMEGA_D=0.66667     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/9th/FD%3D1.1%2COMEGAD%3D0.66667.png)        
**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007
