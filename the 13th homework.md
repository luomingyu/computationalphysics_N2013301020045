**THE THIRTEENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**BACKGROUND**
--------

- In regions of space that do not contain any electric charges, the electric potential obeys **Laplace's eqaution**        

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式1.png)           
 
From a numerical perspective the situation here is a bit different from anything we have encountered so far, All of our problems to this point have involved differential equations for which several initial conditions were given, and we were able to use the **Euler method** or something like it to calculate the behavior for later times. However, with **Laplace's equation** we are generally given some boundary conditions for **V**, which specify its value on a surface in **x-y-z** space. Alternatively, the boundary conditions might be given in terms of the electric field, which is proportional to the gradient of **V**. In either case our problem is to find the function **V(x,y,z)** that satisfies both Laplace's equation and the specified boundary conditions. Most importantly, satisfying the boundary conditions will not be as easy as with the ordinary differential equations encountered in previous chapters.                           

  
**METHOD**
----

- We now require a numerical strategy for determining this function, assuming only that **V** is known at the boundaries. We can't just start at one of the boundaries and work our way into and across the system since according to:                   

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式4.png)           

we need to know **V** at all of the neighbors in order to calculate its value at any particular point. The approach we take is to begin with some initial guess for the solution; call it **V_0(i,j,k)**. In general, unless we are extremely clever, the guess we make will not satisfy the above everywhere. To obtain an improved guess, we use it to calculate new values of **V**, using **V_0** on the right-hand side. The guess **V_0**, together with it yields, a new and we hope improved guess, **V_1(i,j,k)**. We then repeat the procedure with **V_1** to obtain an even better guess, **V_2**, etc. This iterative process is continued until our result satisfies some convergence criteria, which we will discuss shortly. The general approach is called the **relaxation method**, and is a useful way to deal with several important classes of partial differential equations. There are different ways to implement the relaxation method, and some are much better than others with respect to speed of convergence, etc.         

**MODEL**
----
- As usual we discretize the independent variables, in this case **x**, **y** and **z**. Points in our space are then specified by integers **i**, **j** and **k**, with **x=i*delta x**, **y=j*delta y**, **z=k*delta k**. Our goal is to determine the potential **V( i, j, k ) = V( x=i*delta x, y=j*delta y, z=k*delta k)** on this lattice of points. The first step in reaching this goal is to rewrite          

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式1.png)           

as a difference equation. We already know how to write a first derivative in finite-difference form. For example, at the point **( i, j, k )** the derivative with respect to **x** may be written as       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式2.png)           

- Finally, we found      

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式3.png)           

where we have assumed that the step sizes along **x**, **y** and **z** are all the same **( delta x = delta y = delta z )**. In words, these simply says that the value of the potential at any point is the average of **V** at all of the neighboring points. The solution for **V( i, j, k )** is the function that manages to satisfy this condition at all points simultaneously.      

- From the symmetry it is natural to suppose that the potential on these surfaces of the box will vary linearly with position as we move from **x=-1** to **x=+1**. We assume further that the box is infinite in extent along **+-z**, so **V( i, j, k )** is independent of **k**. We thus have only a two-dimensional problem. Our goal is to find the potential function **V( i, j )** that satisfies       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式5.png)           

- Finally, if we wish to obtain the electric field, this can be calculated by differentiating **V( i,j )**. To do this we use the fact that the component of **E** in the **x** direction is       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式6.png)           

with corresponding relations for **E_y** and **E_x**. These dericatives can be estimated using our usual finite difference expressions. In this case we can use a symmetric form for this derivative       

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/公式7.png)           

but a lesss symmetric form would give essentially the same results. One note of caution is that **E** at the boundary needs to be calculated using a one-sided difference equation since, clearly, using values of **V** at sites beyond the boundary makes no sence.       
- Another interesting use of the relaxation algorithm is the problem of the potential between two parallel capacitor plates. The case of infinite plates can, of course, be handled analytically using Gauss' law. However, here we are intereted in what happens when the plates are finite in extent. Again, we can modify our earlier program to handle this case. All we need to do is set up the proper boundary conditions for **V**. We set the plates to **V=+-1**, and the square boundary defined by **x=+-1**, **y=+-1** surrounding the plates is set to **V=0**. In analytic calculations we would generally apply the condition **V=0** at **x,y** approximate to indinite, but that is usually not pracical in a numerical treatment. Here, for simplicity, we apply this condition on the square boundary just describled; we will have more to say about how to choose such boundary regions and their effects in the next section. After specifying the boundary conditions on **V**, the application of the relaxation algorithm is the same as that outlined above. The electric field is seen to be largest between  the two plates. In that region the field is approximately uniform ( although this is hard to verify with the rather coarse scale used for this plot ) and is directed from high to low potential. The fring fields at the edges of and outside the plates are also evident.      

**EXERCISE**
--

- **5.3** Use the symmetry of the capacitor problem to write a program that obtains the result by caculating the potential in only one quadrant of the **x-y** plane.
         
- **result**
- 
- [code for the relaxation method](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/relacation%20method.py)
--
- [code for the SOD method](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/simultaneous%20over-relaxation.py)
--
- We will change the initial conditions, so we find         

V_1=1, V_2=-1, V_B=0
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-0-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-0-1.png)           

V_1=1, V_2=-1, V_B=2
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-2-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-2-1.png)           

V_1=1, V_2=-1, V_B=1
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-1-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1-1-1.png)           

V_1=1, V_2=-1, V_B=-1
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1--1-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1--1--1-1.png)           

V_1=1, V_2=0, V_B=-1
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0--1-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0--1-1.png)           

V_1=1, V_2=0, V_B=0
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0-0-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0-0-1.png)           

V_1=1, V_2=0, V_B=1
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0-1-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0-1-1.png)           

V_1=1, V_2=0.5, V_B=0
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0.5-0-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-0.5-0-1.png)           

V_1=1, V_2=1, V_B=0
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-0-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-0-1.png)           

V_1=1, V_2=1, V_B=1
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-1-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-1-1.png)           

V_1=1, V_2=1, V_B=2
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-2-2.png)           

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/13th/1-1-2-1.png)           

**REFERENCE**
----  
[1] Compulational Phsics , Nicholas J. Giordamo and Hisao Nakanishi , Tsinghua University Press, December 2007           
[2]Thanks for the code to                          
**ChenYangyao/computationalphysics_N2013301020169**
