---
# Sampling of random variables
---
---

## Question :
---


1. Write a program for a lottery ticket number selection by computer.

2. Use the sampling methods you have learned to generate random points according to the Gaussian distribution, and compare with analytical results, and compare the advantages and disadvantages of various methods.

$$ f(x) = \frac{1}{\sqrt{2\pi}} \frac{1}{\sigma} \exp \{ -\frac{(x-\mu)^2}{2\sigma^2} \} $$

---

## Solve:

---

### (1) 

In each福利彩票 (welfare lottery) draw, there are 6 red balls and 1 blue ball. The numbers for the red balls range from 1 to 33, and the numbers for the blue ball range from 01 to 16.

Result:
```
The predicted number is: 
Red Ball Number:[10, 14, 17, 30, 27, 7]
Blue Ball Number:[6]
```

### (2)

#### Result:

1. Direct Sampling Method
---

The direct sampling method is relatively simple compared to other methods, but it can pose certain difficulties because it requires finding the inverse function, and some functions may not have analytical solutions.

![Gauss1](https://github.com/user-attachments/assets/abb016f7-815d-4b09-8caa-3534893217fd)


2. Transformation Sampling Method
---


The transformation sampling method involves transforming the sampling of a complex distribution into the sampling of a known, simpler distribution. This allows for flexible transformation of samples according to needs. However, the transformation process may introduce bias that affects the results.

![Gauss2](https://github.com/user-attachments/assets/7bbd53fb-44d7-420c-a5b7-874f5f86aead)


3. Rejection Sampling Method
---


Rejection sampling involves generating samples uniformly and then accepting or rejecting them based on the desired probability density function. More samples are rejected in areas where the probability density function is high, and fewer are rejected where it is low. Compared to other sampling methods, rejection sampling is relatively simple and easy to implement. However, if there is a periodic correlation between the sampling intervals and the overall characteristics, it may lead to less randomness in the selection of samples, introducing bias. Additionally, the efficiency of sampling may not be high due to the rejection of some data. This is especially true in cases where the probability density function has extremely high values at certain points, which can result in a large proportion of data being discarded and extremely low sampling efficiency.

![Gauss3](https://github.com/user-attachments/assets/25205f86-e197-49e6-bb30-52cfab7e2685)



4. Central Limit Theorem
---

The Central Limit Theorem applies to various distributions, but it requires a sufficiently large sample size. When the sample size is small, it may not approximate the normal distribution well.

![Gauss4](https://github.com/user-attachments/assets/22143a4f-823c-4261-87ba-cd24b78bb972)


5. Second Kind of Rejection Sampling Method
---

The second kind of rejection sampling method first applies rejection sampling to variables with high efficiency, followed by transformation. Compared to the first kind of rejection sampling, it is more efficient and can save time costs. However, it shares the same drawback as the first kind: if there is a periodic correlation between the sampling intervals and the overall characteristics of the population, it may lead to less randomness in the selection of samples, thus introducing bias.

![Gauss5](https://github.com/user-attachments/assets/9c3e1a25-9a25-427a-be26-b807ecf23993)


