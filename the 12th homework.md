**THE ELEVENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

- To this point all of our planetary simulations have involve two-body solar systems. It is now time to consider some of the things that can happen when there are three or more objects in the solar system. The problem of two objects interacting through the inverse=square law can be solved exactly ( as we have already mentioned ), leading to Kepler's laws. However, if we add just one more planet to give what is known as the **three-body problem**, an analytic theory becomes much more difficult. In fact, there are very few exact results in this case, even though it has been studied extensively for several centuries. Indeed, the three-body, or more generally the **n-body problem**, is the problem of celestial mechanics.                  

  
**METHOD**
----

We have used the Euler-Cromer method. That is, we use the previous values of position and velocity to update the velocities, while the previous values of position and the new values of velocity are used to update the positions. As we discussed, the Euler method is not a good choice for oscillatory problems, and planetary motion is just such a problem. If we were to use the Euler method here we would find that the energy od the planet would grow with time, and it would spiral away from the Sun. This difficulty is avioded with the Euler-Cromer method, since it conserves energy exactly over the course of each orbit.:                   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式1.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式3.png)           

**MODEL**
----
- We consider one of the simplest three-body problems, the Sun and two planets, which we will take to be Earth and Jupiter. We know that without Jupiter, Earth's orbit is stable and unchanging with time. Our objective is to observe how much effect the gravitational force from Jupiter has on Earth's motion. We consider Jupiter since, at about 0.1% of the solar mass, it is by far the largest planet in the solat system.      
- Writing **F_E,J** in terms of components yields     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式4.png)                  
for the **x** component of the force, with a corresponding result for the **y** component. Here **x_e** and **x_j** are the coordinates of Earth and Jupiter ( the Sun remains at the origin ), and **theta_E,J** is the angle defined. The total force on Earth in the **x** dirction will be the sum of the forces of gravity from the Sun and Jupiter, yielding the equation of motion for the **x** component of Earth's velocity, **v_x,e**       
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式5.png)                  
where **r** is again the distance from Earth to the Sun. We can convert this and the corresponding result for **v_y,e**, into difference equations. Since **M_S** is much greater than **M_J** or **M_E**, we may treat the Sun to be stationary at the origin and just calculate the positions of Jupiter and Earth. Thus, the only thing left to do is calculate **GM_J** in the appropriate units, Here it is simplest to use the result        
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/公式6.png)                  
with **M_J** and **M_S** given. A program to calculate the orbits of two planets in this approximation is a straightforword extension of the one we sketched for the two-body solar system previously. We now need to update the positions and velocities of both planets at each step through the main loop. A sketch of such a calculation is given.     
- Some results from this simulation are shown in following:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-1.png)                  
Using parameters appropriate for Earth and Jupiter, we find that both of the planets follow stable circular orbits. Thus, Jupiter has a negligible effect on Earth ( at least on this scale ). This should not be terribly surprising; we know that Earth has been orbiting the Sun for several billion years, so the orbit must be fairly stable! We can also use our simulation to calculate what would happen if the mass of Jupiter were somehow increased. Giving Jupiter a mass of **10M_J**, that is, 10 times its actual value, has no discernible effect on Earth ( at least on the scale of this figure ).     
- It is tempting to see what would happen if the mass of Jupiter were increased to **100M_J** or even to **1000M_J**, using the same program. However, since **1000M_J** is about equal to the mass of the Sun, the perturbation by Jupiter on the Sun would then be significant and would have to be taken into account. If we ignore this detail, and simply use **1000M_J** as the mass of the second planet in routine, we find the interesting trajectory shown in following:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-1.png)                  
We see that Earth's orbit becomes completely unstable, as it is eventually ejected from the solar system! To investigate this problem more carefully, we need to perform a true three-body calculation, in which the motion of all three bodies - the Sun, Jupiter, and Earth - are computed. The results of such a simulation are very sensitive to the initial conditions, and often quite dramatic.       

**EXERCISE**
--

- **4.16** Carry out a true three-body simulation in which the motions of Earth, Jupiter, and the Sun are all calculated. Since all three bodies are now in motion, it is useful to take the center of mass of the three-body system as the origin, rather than the position of Sun. We also suggest that you give Sun in initial velocity which makes the total momentum of the system exactly zero ( so that the center of mass will remain fixed ). Study the motion of Earth with different initial conditions. Also, try increasing the mass of Jupiter to 10, 100, and 1000 times its ture mass.      
         
- **result**
- 
- First
- 
- [code1](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/SUN-fixed.py)
--
- assumeing the Sun is fixed, the growth rate of the Juiter equals 1, so we found：          

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-1.png)         

Gradually enlarge the earth's orbit, a little disturbance happened.       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-2.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-3.png)         

The same thing happened to the Jupiter.            

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-4.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1-5.png)         

- If inceace the growth rate to 10, it is the same as above     

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/10-1.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/10-2.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/10-3.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/10-4.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/10-5.png)         

- When the rate turns to 1000, something really differently happened compared to the 1 or 10.       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1000-1.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1000-2.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/1000-3.png)         

- Second    
----
- [code2](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/realthree_bodies.py)
--
- We make the Sun unfixed, it is the real three-bodies motion. Let the growth rate equals 1, 10, 100, and 1000.        

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/u-1.png)         

- If the initial angle between the Earth and Jupiter is different, what will happen with the growth rate is 100?         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/u-2-1.png)         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/U-2-2.png)         

- This situation also happened with growth rate is 1000.       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/u-3-1.png)         

This above picture amplify like:     

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/u-3-1-1.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/12th/u-3-2.png)           

[code](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/q1-1.py)
--

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007