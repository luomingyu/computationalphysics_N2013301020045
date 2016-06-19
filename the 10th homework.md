**THE TENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

The model that we have considered so far in this chapter - the pendulum - is very simple system, yet it exhibit extremely rich behavior. It is thus not surprising that other slightly more complicated systems are also capable of chaoic behavior. When we think of chaoic or unpredictable behavior, an example that naturelly comesto mind is the weather. Because of the economic importance of having accurate weather predictions, a good deal of effort has been devoted to this problem. While much of this effort has gone into computer modeling of Earth's atmosphere, much has also been devoted to understanding the weather problem from a more fundamental point of view. It was work of this kind by the atmospheric scientist E. N, Lorenz that provided a major contribution to the modern field of chaos.           
  
  
**METHOD**
----

- It turns out that the Euler algorithm can actually br used to treat the Lorenz problem, for the following reason. Several of the terms in the Lorenz equations play the same role as the damping term in the pendulum equation of motion, while other terms are analogous to the driving force. If the time step in the Euler algorithm is sufficient small, the energy lost ( or added ) through the error terms associated with the Euler method can be made much small than the energy lost to the effective damping, or added by the effective driving force. In this situation, the **Euler method** provides an accurate solution, as can be verified directly by simply repeating the **Euler** calculation with the **Runge-Kutta method**:                   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/公式1.png)           
- It turns out

**MODEL**
----
- Lorenz was studying the basic equations of fluid mechanics, which are known as the Navier-Stokes equations; they can be thought of as Newton's laws written in a form appropriate for a fluid. These are a complicated set of differential equations that describe the velocity, temperature, density, etc., as functions of position and time, and they are very different to solve analytically in cases of practical interest. The specific situation he considered was the Rayleigh-Benard problem, which concerns a fluid in a container whose top and bottom surfaces are held at different temperatures. It had long been known that as the difference between these two temperatures is increased, the fluid can undergo transitions from a stationary state ( no fluid motion ) to steady flow ( nonzero flow velocities that are constant in time, also referred to as convection ) to chaoic flow. Indeed, Lorenz grossly oversimplified the problem as Lorenz reduced it to only three equations:          
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/公式2.png)           
These are now known as the Lorenz equations ( or equivalently, the Lorenz model ). The Lorenz variables **x**, **y** and **z** are derived from the temperature, density, and velocity variables in the original Navier-Stokes equations, and the parameters **sigma**, **tau** and **b** are measures of the temperature difference across the fluid and other fluid parameters.      
- Returning to the Lorenz problem, these are three parameters **sigma**, **tau** and **b**, and the behavior one finds dependd on their values. We will follow custom and use **sigma=10** and **b=8/3**. According to some authors these values correspond to cold water, but given the highly simolified nature of the model you shouldn't take this claim seriously! The parameter **tau** is a measure of the temperature difference between the top and bottom surfaces of the fluid. For small **tau** the effective force on the fluid. As **tau** increases this force increases, so **tau** plays a role analogous to the frive amplitude, **F_D**, in the pendulum problem. Results for **z** as a function of time are shown in following:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图1.png)           
which shows the behavior at three different values of the force **tau** ( **x** and **y** exhibit qualitatively similar behavior ).            
- At **tau=5** there is an initial transient, and afer it decays away **z** is a constant, independent of **t**. The same behavior is seen at **tau=10** , although the transient takes a little longer to decay. These two cases correspond to steady convective moiton in the original fluid; in this process the warm fluid produced at the bottom surface of the container rises and the cooler fluid returns from the top. This  steady convection is the analog of regular nonchaotic motion of the pendulum. The behavior is completely different at **tau=25**. Here the initial transient is roughly periodic, but it givees way to an irregular, that is chaotic time dependence after **t=20** or so. There are not many exact results available for the Lorenz model, but it is known that the transition from steady convection to chaoic behavior takes place at **tau=470/19**.      
- We found that a **Poincare section** can reveal underlying regularities that are not obvious from the time dependence alone.  With this motivation we consider how to construct sucha phase-space plot for the Lorenz model. The situation here is a little more complicated than that of the pendulum, since we now have three variables to deal with, **x**, **y** and **z**, as opposed to only two in the pendulum problem ( **theta** and **omega** ). There are several ways to proceed. Perhaps the simplest way is to imagine that **x**, **y** and **z** are coordinates in some abstract space and recongnize that we are dealing with a trajectory in this space. We can then obtain a projection of thos trajectory by simply plotting **z** as a function of **x**; this gives a projection onto the **x-z** plane. Such a projection for the chaoic case **tau=25** is shown in following:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图2.png)           
3d
![x](https://github.com/luomingyu/computationalphysics_N2013301020045/blob/code/10th/书图2-3d.gif)           
In this trajectory the system undergoes approximately periodic oscillations ( roughly circlar orbits ) on one side of t;he line **x=0**, then moves to the oposite side of this line and undergoes a new series of oscillations,ect.     
- However, in the Lorenz model there is no direct analog to this drive force with its sinusoidal time dependence, so we must take a slightly different approach. We already mentioned that the Lorenz variables **x**, **y** and **z** can be viewed as specifying the trajectory of a particle moving in three dimensions. It is then natural to consider two-dimensional slices through this trajectory. To be more specific, we show on the left in following     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图3-1.png)           
Which is a plot of **z** verse **y** when **x=0**. In our trajectory lauguage, we are simply plotting the places where the trajectory intersects the **y-z** plane. The results in following       
 ![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图3-2.png)           
were obtained with **tau=25**, which, as we have already seen, places us in the chaoic regime. We see from the figure that even through the behavior is strongly chaoic, there is a very high degree of regularity in the phase-space trajectory. This attractor surface in phase-space can be shown to be independent of the initial conditions. Hence, while the time-independent behavior is unpredictable, we can predict with certainty that the system will be found somewhere on the **attractor surface** in phase-space.     

**EXERCISE**
----
[**code**](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/tu1.py)          
--
- **3.26** Continue the previous problem, and construct the phase-space plots as in the different regimes.             

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图3-1.png)                 
 ![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/10th/书图3-2.png)           

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007
