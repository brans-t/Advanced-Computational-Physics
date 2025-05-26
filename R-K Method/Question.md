# R-K Method

---

## Question :
---

Numerically solve the following in the interval \[0, 16\]:

$$
\begin{cases}
y' = y - \frac{2x}{y} \\
y(0) = 1
\end{cases}
$$

(1) Use the classical Runge-Kutta (R-K) method with step size \( h = 0.2 \).

(2) Use the Adams-Bashforth-Moulton predictor-corrector method to solve the above problem with step size \( h = 0.1 \), starting with the classical R-K method.

(3) Use the variable step size Adams-Bashforth-Moulton predictor-corrector method to solve the above problem, with an initial step size \( h = 0.1 \).

(4) Use MATLAB's ode45 to solve the above problem.

---

## Solve:

---
(1)
![RK1](https://github.com/user-attachments/assets/60e214ef-6e08-4db0-b20d-39c4a29cc000)

![RK1.png](R-K Method/figure/RK1.png)

(2)
![RK2.png](R-K Method/figure/RK2.png)

(4)
![RK3.png](R-K Method/figure/RK3.png)
