# Development II 

## Spring 2018



Jonathan Conning

**Hunter College and The Graduate Center*** 

**City University of New York**

---

## Week 2: Why isn't the whole world developed?

- Technology and other assumptions
- Neo-classical benchmarks
  - Efficient allocation and convergence
    - Solow Growth 
    - Trade 
    - Factor movement
- Misallocation
  - Lewis, dualism and its critics
  - enduring puzzles
  - modern takes

---

Lucas, Robert E. 1990. “Why Doesn’t Capital Flow from Rich to Poor Countries?” *American Economic Review* 80 (2): 92–96. [link](https://docs.google.com/viewer?url=https%3A%2F%2Fwww.econ.nyu.edu%2Fuser%2Fdebraj%2FCourses%2FReadings%2FLucasParadox.pdf)  

Gollin, Douglas. 2014. “The Lewis Model: A 60-Year Retrospective.” *Journal of Economic Perspectives* 28 (3): 71–88. [link](https://sites.google.com/site/douglasgollin/doug-gollin/research)

Gollin, Douglas, David Lagakos, and Michael E. Waugh. 2013. “The Agricultural Productivity Gap.” *The Quarterly Journal of Economics* 129 (2): 939–993. ([link](https://sites.google.com/site/douglasgollin/doug-gollin/research))

Also useful: [jupyter notebooks](http://dev-ii-seminar.readthedocs.io/en/latest/index.html) on Specific Factors, Edgeworth Boxes and Lucas 1990.

---

## Homogeneous and Homothetic Production Functions

A function is homogenous of degree $k$ if:

$$F(\tau K,\tau L)=\tau^k F(K,L)$$

Linear-homogeneous or constant returns (k=1): 
$$F(\tau K,\tau L)=\tau F(K,L)$$

Production in intensive form.

 If k=1, set $\tau =\frac{1}{L}$ :  $F(\frac{K}{L},1) = \frac{F(K,L)}{L}=f(k)$

where $k=\frac{K}{L}$

---

## Euler's Theorem

Recall 
$$F(\tau K,\tau L)=\tau^k F(K,L)$$

Take derivative wrt to $\tau$

$$k \cdot \tau^{k-1} F(K,L)=F_K \cdot K + F_L \cdot L$$

When $k=1$ (CRS)

$$F(K,L)=F_K \cdot K + F_L \cdot L$$

---

On competitive markets $r=p \cdot F_K$  and $w=p \cdot F_L$ so we get

$$F(K,L)=F_K \cdot K + F_L \cdot L$$

$$p \cdot F(K,L)=p \cdot F_K \cdot K + p \cdot F_L \cdot L$$

$$p \cdot F(K,L)=r \cdot K + w \cdot L$$

Factor payments exhaust total product

---

When $k=1$ Euler's theorem in intensive form means marginal product of capital will be $f'(k)$ and marginal product of labor (wage in competitive model):

$$f(k) - f'(k) \cdot k$$

output per worker hour minus payments to capital per worker hour equal wage per worker hour.

---

If $F$ is homog. of degree $k$, marginal products are homog. of degree $k-1$.  

Take derivative of each side of $F(\tau K,\tau L)=\tau^k F(K,L)$ wrt to $K$ and $L$ respectively:

$$F_K(\tau K, \tau L)=\tau^{k-1}F_K(K,L)$$

$$F_L(\tau K,\tau L)=\tau^{k-1}F_L(K,L)$$

Implies that the rate of technical substitution (RTS) or the slope of any isoquant along any ray from the origin is the same:

$$\frac{F_L(\tau K, \tau L)}{F_K(\tau K, \tau L)}=\frac{F_L(K,L)}{F_K(K,L)}$$

------

With Constant Returns to Scale ($k=1$)

$F_L(\tau K, \tau L)=F_L(K,L)$ and $F_K(\tau K, \tau L)=F_K(K,L)$

In a competitive market all firms hire $K$ and $L$ to equalize factor prices. Means can determine only $\frac{K}{L}$ ratio and not scale of $K$ and $L$. Any two firms with same have the same $\frac{K}{L}$ have same marginal products $F_K$ and $F_L$.  

Hence with CRS the size distribution of firms is *indeterminate*

Firms could be all the same size, some large other smalls.  We can't tell, nor does it really matter. 

Another way to see this: under CRS marginal and MC(Q) and AC(Q) of production are same across firms. So cannot determine firm's optimal scale Q.

---

## Cobb-Douglass production 

$$F(K,L) = A \cdot K^\alpha L^\beta$$

$A$ interpreted as total factor productivity parameter

Degree of homogeneity $k=\alpha +\beta$

---

If $k=1$ then $\beta=1-\alpha$, then  

$$F_L = (1-\alpha) A \cdot K^\alpha L^{-\alpha}= (1-\alpha) A \cdot \frac{K^\alpha L^{1-\alpha}}{L}$$

$$F_L= \frac{(1-\alpha) \cdot F(K,L)}{L}$$

and 

$$F_K= \frac{\alpha \cdot F(K,L)}{L}$$

Marginal products are a multiple of average products

---

# Aggregate Production Function Models

- Solow Growth Model 
- Convergence in any model with diminishing returns to the accumulated factor (guaranteed with CRS )

---

## Solow Growth Model

$y=k^\alpha$

$\frac{dk}{dt} = s \cdot k^\alpha - (n+g+\delta) k$

Steady state:  

$$k^* = \left( \frac{s}{n+g+\delta}  \right )^\frac{1}{1-\alpha}$$

Convergence regardless of starting point.

Countries further away from steady state grow faster (catch up or converge)

---

## Capital mobility

Diminishing marginal product of capital implies that countries that if there are two countries with the same production technology 

- country with less accumulated capital per worker has higher $r=f'(k)$
- capital should flow from rich to poor countries, accelerating convergence.

See Lucas (1990) [jupyter notebook](http://dev-ii-seminar.readthedocs.io/en/latest/notebooks/Lucas90.html)

---

# Ricardo-Viner or Specific Factors Model

Variations of the model (see [jupyter notebook](http://dev-ii-seminar.readthedocs.io/en/latest/notebooks/SFM.html))

- Two-sector trade model (short-run version of Hecksher-Ohlin-Samuelson or HOS model)
  - Income distribution and Political economy
- Migration across countries, sectors
  - dualism, Lewis, Harris Todaro
- (mis)allocation across and within sectors.


---

## Institutions as Fundamental 