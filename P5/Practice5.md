# Softwarehomework 5
## 03015434

### 1、Description

#### （1）Problem：IAPWS-IF97 physical properties calculation and unit test 

#### （2）Particular requirements：

* According to the Revised Supplementary Release on Backward Equations for Specific Volume as a Function of Pressure and Temperature v(p,T) for Region 3 of the IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water and Steam http://www.iapws.org/relguide/Supp-VPT3-2016.pdf calculation formula provided,design physical properties calculation and unit test program

 * 1 physical properties calculation：StudentID 030153434 ->3h subregion,realize the ***Supp-VPT3-2016.pdf*** supplementary formula of the v(p,T) calculation.

 * 2 unit test program：Test unit based on physical property calculation program in the **unittest**.

### 2、Solution

#### （1）Physical properties calculation

* Use the following supplementary formula *v（p，T)* to caculate：
$$ \frac{v(p,T)}{v^*}=\omega(\pi,\theta)=[\sum_{i=1}^n n_i[(\pi-a)^c]^{I_i}[(\theta-b)^d]^{J_i}]^e $$
 * $ \omega=v/{v^*},\pi=p/{p^*},\theta=T/{T^*} $，
 
 * Find the $ v^*,p^*,T^*,N,a,b,c,d,e $ in *IF97-dev,Table 4,3h*，$ n_i，I_i，J_i $ in *Table A1.8*
   
 * The volume v is obtained by **While** cycle accumulation calculation.

#### （2）Unit test program

* unittest module is a unit testing framework that comes with Python, which encapsulates some result methods of check return and       initialization operation before execution of some use cases.
* execute the test case through unittest.mainer.