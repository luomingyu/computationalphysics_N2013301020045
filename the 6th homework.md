**THE SIXTH HOMEWORK**
====

No.:2013301020045     
NAME：罗明宇

**PROPOSE**
--------
Finish the Exercise 2.10 involving the wind resistance and set up a precise hitting system to assist people.

**METHOD**
----

- If we ignore air resistance , the equtions of motion , thich are obtained from Newton's second law,we written as     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/1.png)      
We can write these equations as     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/2.png)         
To use the Euler method , we write each derivative in finite difference for as     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/3.png)      
We assume the magnitude of the drag force on our cannon shell is given by     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/4.png)     
and we find     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/5.png)     
Adding the components of the force to the equations of motion leads to     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6.png)      

so I scan the range of the firing angle [the code of scanning](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-最优角度判定-风阻.py) like        
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-最优角度判定-风阻.png)     
and use the best angle which lead to the longest firing distance [the code of the route of the cannon shell](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-路径-风阻.py) to gain the route like        
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-最优角度路径-风阻.png)     

- But the density of sir will affect air resistance , and it vary as a function of the altitude . So we have a somewhat different dependence of the density on altitude by adiabatic approximation            
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/7.png)           
The drag force due to air resistance is proportional to the density , so     
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/8.png)            
Finally , we gain the equations of motion leading  to           
![x](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/9.png)           

we can use [the code of scanning](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-最优角度判定-风阻%2B空气密度.py) to choose the best angle which lead to the longest distance of cannon shell and gain [the corresponding route](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-路径-风阻%2B空气密度.py) . 
We also can set the aimming distance to gain the corresponding angel and initial vecolicy [the code of amming distance](https://raw.githubusercontent.com/luomingyu/computationalphysics_N2013301020045/code/6th/6th-定点打击扫描-风阻%2B空气密度%20-%20.py) . (The code need to be simplified to run . because I haven't found the bug , but my computer cannit run this file )     


----
