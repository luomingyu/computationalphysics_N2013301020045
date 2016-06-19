**THE FORTEENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

- We consider several topics associated with wave motion. While the central ideas in this discussion are applicable to virtually all types of waves, we will find it convenient to consider the particular case of waves on a string. After introducing and developing a solution for the wave equation in the ideal case ( that is, for a perfectly flexible, frictionless string ), we then extend our modeling to deal with waves in several more realistic situations. This will lead us to some interesting issues that arise in connection with musical instruments.                                  
  
**METHOD**
----

- Our main job in this section is to develop a numerical scheme for solving the wave equation. Superficially, it bears some resemblance to Laplace's equation, as both contain a second-order spatial derivative. However, with it we wish to solve for the time-dependent solution **y(x,t)** rather than a stationary solution. Thus, the relaxation methods described are not suitable. We must therefore attack the wave equation with rather different numerical treatments than those that we employed in our work with Laplace's equation. After we develop an algorithm suitable for it, we will use it to explore several aspects of wave motion and also the behavior of more realistic models, including the stiffness of the string ( which leads to an effect known as dispersion ) and friction ( i.e., damping ). The method we use is introduced in following.                  

**MODEL**
----
- The central equation of wave motion is       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式1.png)           

which is usually referred to as the wave equation. This equation arises in many situations, including waves on a string, electromagnetic waves, waves on the surface of a lake, and sound waves. Here we will use a language appropriate for waves on a string, although our methods and conclusions will apply to other cases as well. **y** is then the displacement of the string from its equilibrium (undisturbed) form. **x** is distance measured along the string, **t** is the time, and **c** is a parameter that turns out to be the speed with which a wave moves on the string.         
- We obtain         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式2.png)           

- To construct a numerical approach to the wave equation, we will, as usual, write it in finite difference form. We treat both **x** and **t** as discrete varibles with **x = i*delta x** and **i = n*delta t**. The displacement of the string is then a function of both **i** and **n**, which we write as **y(i,n) = y( x = i*delta x, i = n*delta t )** so that the first index of **y** specifies the spatial coordinate and the second index corresponds to time. We have already the needed expression for the second partial derivative, and inserting it into the wave equation yields.         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式3.png)           

This problem is in some respects similar to the initial-value problems we enconuntered. In those cases we typically considered the time-dependent motion of an object using an equation of motion that was derived from Newton's second law. In order to obtain a solution for those differential equations we required some initial conditions, which were often the posotion and velocity at an initial time. To construct a solution we will also require some initial conditions. For simplicity we will assume that the displacement of the string at times prior to and including **t_n = n*delta t** is known. We then want to derive an expression for the displacement at the next time step, **t_(n+1) = (n+1)*delta t**. Rearranging it we can express **y(i,n+1)** in terms of **y** at previous time steps, with the result         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式4.png)           

where **r = c*delta t/delta x**. Thus if we know the string condiguration at time steps **n** and **n-1**, we can calculaate the configuration at **t = 0**, which we will refer to as **y_0(x)**. Since we are dealing with a second-order differential equation, we require two initial conditions. Knowledge of the string configuration at two consecutive time steps is thus sufficient. One natural choice, and the one that we will make here, is to assume that the string is held fixed with shape **y_0(x)** prior to **t = 0**.        
- There is one more important issue that must be dealt with, namely how to treat the ends of the string. We have several options; perhaps the simplest choice is to treat the ends as fixed, that is, tied down so that they can't move ( y(0,n)=y(M,n)=0 ), and then restricting the updating of **y(i,n)** to the interior of the string ( the region extending from **i = 1** to **i = M-1** ) using it. However, we might also want to consider different boundary conditions, such as free ends, or ends that are intermediate between  fixed and free. For example, to see how to implement free ends. The first term on the right is the force exerted on segment **i** by the string segment **i+1** on its right, while the second term is the force from segment **i-1** on the left. If we now consider the motion of the left end, **i=0**, which is assumed to be free, only the first term will be present. We see that the corresponding equation of motion for the end segment **y_0** must have the form       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式5.png)           

We will see shortly that the boundary conditions greatly affect the manner in which waves are reflected when they reach the ends of the string.     
- The uppermost plot is the initial ( **t = 0** ) displacement of the string. Here we have assumed a simple "Gaussian pluck" of the string. That is, we have taken the initial string profile to be         

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/公式6.png)           

where the displacement is centered at **x_0**, and **k** is a factor that determines the width of the Gaussian envelope. We use  **x_0 = 0.3 m** and **k = 1000 m^-2**, and the string runs from **x = 0 to 1 m**. We have included units here as we will be applying some of these ideas to ( semi- ) realistic piano strings in the following sections.       

**EXERCISE**
--

- **6.6** An important feature of a linear equation is that the sum of two solutions is also a solution. One consequence of this is that two wavepackets will travel independently of each other. An especially clear way to demonstrate this is to set up a string with an initial profile such that there are two Gaussian wavepackets, located at different places in the string. These eavepackets ( or components of them ) may then propagate toward each other and collide. Show that the wavepackets are unaffected by these collisions. This is, show that two such wavepackets pass through each other without changing shape or speed.      
         
- **result**
- 
- [code](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/14th/temp.py)
--

r1=0.75, r2=0.45         
![x](https://github.com/luomingyu/computationalphysics_N2013301020045/blob/code/14th/1.gif)           

 r1=1, r2=0.45        
![x](https://github.com/luomingyu/computationalphysics_N2013301020045/blob/code/14th/1.gif)           
     

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007           
[2]Thanks for the code to                          
**ChenYangyao/computationalphysics_N2013301020169**
