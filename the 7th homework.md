**THE SEVENTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**EXERCISE 2.19**
--------

Model the effect of backspin on the range of a batted ball . Assume an angular velocity of 2000 rpm (I consider it as 2000 rad per minute)


**METHOD**
----

- In order to calculate the trajectory of a baseball,we need to solve the Euler equations , including the velocity dependence of the drag force . Taking the results for the drag coefficient and adding in the appropriate factors of air density , and so on , it turns out that the drag factor for a normal baseball is described reasonably well by the function              
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/formula1.png)           
with           
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/formula2.png)     
         
- To treat the problem of  a thrown ball , we must deal with two different effects . One effect is the spin of the ball ; this will turn out to dominate the motion of a curve ball . The other effect concerns the drag coefficient .     
To calculate the trajectory of a curve ball , we have to consider motion in three dimensions . We will let **x** be the axis running from home plate to the pitcher , **z** be the horizontal direction perpendicular to **x** , and **y** be the height above the ground . So the equations of motion for a sidearm curve ball are then     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/formula3.png)      

![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/formula4.png)      
Here we assume that the axis of rotation is parallel to **y** , that is , perpendicular to the ground . These equations of motion include the effect  of atmospheric drag on the largest component of the velovity (Vx) , with a velocity dependent coefficient , but we haven't included it for Vy or Vz , since the forces are much smaller in these cases .   
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/3.gif)

[code](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/7th/baseball%20without%20wind.py)
---
Thanks for [Huang Xudan's help](https://github.com/tongqiancao/computionalphysics-N2013302290059)
----
