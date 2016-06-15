**THE ELEVENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

- In the present chapter we found that  atmospheric drag plays a role in the behavior of projectiles moving near the earth's surface. In some respects, this drag and other types of "friction" obsure the fundamental physics principles that govern the behavior. If we want to study the essential consequences of these principles, it thus seems best to consider a system in which frictional forces are as small as possible. The solar system is just such a laboratory, and not surprisingly, studies of the motion of planets and moons provided major inspiration to the founders of classical mechanics.
- We will consider several problems that arise in the study of planetary motion. We begin with the simplest situation, a sun and a single planet, and investigate a few of the properties of this model solar system. While a computational approach is not required in this case, the algorithm we develop will prove useful for later problems. Additionally, comparisons of the numerical results obtained with this algorithm with exact solutions will provide valuable insight into the nature of our approximations.               
  
  
**METHOD**
----

We have used the Euler-Cromer method. That is, we use the previous values of position and velocity to update the velocities, while the previous values of position and the new values of velocity are used to update the positions. As we discussed, the Euler method is not a good choice for oscillatory problems, and planetary motion is just such a problem. If we were to use the Euler method here we would find that the energy od the planet would grow with time, and it would spiral away from the Sun. This difficulty is avioded with the Euler-Cromer method, since it conserves energy exactly over the course of each orbit.:                   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/1.png)           


**MODEL**
----
- However, before we proceed with that, it is useful to consider the choice of units. One option is to simply use **SI units**. There is no difficulty with this except that meters and seconds do not match the scale of the problem. For example, the radius of Earth's orbit is ~1.5*10^11 m. If we were to use **SI** units, a graph showing this orbits around the Sun would have lables of 1*10^11, 2*10^11 m, etc. This would be awkward, though not impossibly so. It is much more convenient to use **astronomical units**, **AU**, which are defined as follows. One astronomical units of length, known simply as **1 AU**, is the average distance between the Sun and Earth ( =1.5*10^11 m ). It is convenient to measure time in years ( 1 year=3.2*10^7 s ) since this unit matches the solar system better than, say, seconds. For the remainder of this chapter we will, therefore, use astronomical units for distance, and measure time in years, unless specifically noted otherwise.       
- To complete our system of units we also need the corresponding unit of mass. This is easily derived if we recall that Earth's orbit is, to a very good approximation, circular. For circular motion we know that it leads to:      
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/2.png)           
where **v** is the velocity of Earth. Rearramgomh we find:     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/3.png)           
where we have used the fact that ( since the orbit is circular ) the velocity of Earth is 2pi*r / ( 1 yr )=2pi ( AU/yr ) ( recall that r=1 AU ). Since G and M_S appear only as aproduct there is no need to express either term separately.     
- We next convert the equations of motion into difference equations in preparation for constructing a computational solution. We find:      
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/1.png)           
where, as usual, **delta t** is the time step and the factors of **4pi^2 ( =GM_S )** signal that we are using astronomical units.     
- We have used our planetary orbits program to simulate the motion of Earth, and the results are shown in:      

- [code of following picture](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/shutu1.py)
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/书图1.png)           
To perform this calculation we need to specify the initial conditions. As we have already noted, Earth's orbit is circular to a very good approximation. We knew that the radius of the orbit is **1.00 AU** ( which we already knew from the definition of astronomical units ), so for our simulation we have chosen an initial **x** coordinate of **1.0** and a **y** coordinate of **0**. It is crucial that we alse choose the proper initial velocity to obtain a circular orbit. To estimate the value required to yield a circular orbit we recall that Earth completes one orbit in one year. The velocity is thus **2pi*r/1 = 2pi AU/yr**. Using these initial conditions we obtain the nicely circular orbit shown. If we had let the program run for mant orbits, we would have found that the calculatd path of the Earth repeats itself to within the size of the points in the figure. We will see below that this repeatability is a general feature of closed orbits in a two-body solar system; that is, a system with one planet and one sun. The result also demonstrates that the Euler-Cromer method is quite suitable for solar system calculation, and we will use it throughout this chapter.     
       
**EXERCISE**
--

- **4.7** Consider a hypothetical solar system consisting of a sun and one planet in which the mass of the sun is not much greater than the mass of the planet. Now you must allow for the motion of both the planet and the sun. Extend your planetary motion program to include this effect. You will have to deal with a set of equations such as those in       
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/1.png)                
for both objects. Investigate the possible types of orbital motion found in such a system. Begin with a double star system in which the two objects are of equal mass. Then explore the behavior when the masses are unequal.  **Hunt**: In order to obtain the simplest orbits, it is best to pick initial conditions such that the total linear momentum is zero. While this problem can be handled with a stationary sun together with the concept of a reduced mass, this calculation is a necessary prelude to the study of orbits of planets in binary star systems, which we will consider in a later exercise.          
- result
- 
- **First**, assume one of the two bodies is the center of the motion system. According to that, useing the reduced mass is a necessary option to simplify the probelm like：     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d1.png)         
with assuming that     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d2.png)         
so it leads to these equations ：     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d3.png)         
By using Euler-Cromer method, we could find      
 ![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d4.png)         

[code](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/q1-1.py)
--
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/q1-1.png)         


- **Second**, translate the motion in the m1-center system to thecenter of mass frame. Regarding the center of mass is fixed, we could find the relative motion equations like      
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d5.png)                
     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d6.png)              
       
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d7.png)           
           
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/d8.png)                
According to that, we also canset the initial parameter of m1 or m2, including **x,y** coordinate and velocity, ect. 

[code](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/q1-2.py)
--       
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/11th/q1-2.png)                

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007