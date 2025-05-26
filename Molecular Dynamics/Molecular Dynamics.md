---
# Molecular Dynamics
---
---
- 1. Write a program using the Verlet velocity algorithm to solve the two-dimensional molecular motion equation.
- 2. Write a two-dimensional program with periodic boundary conditions for a cell of size L.
- 3. Perform a molecular dynamics simulation of a single-atom system at a fixed temperature. The cell length is 10. The number of atoms in the cell is 64. The atomic mass is 1. Use the Lennard-Jones potential, where ε=σ=1, with periodic boundary conditions. The initial positions are randomly distributed, and the initial velocities are randomly distributed between [-1, 1]. The system temperature is fixed at 0.85, perform a molecular dynamics simulation. Provide the relationship between kinetic energy and time, and analyze the velocity distribution after the system reaches equilibrium.
 ---

## Solve:
---
### (1) 

The following is the equation of motion for the uniform rectilinear motion of a two-dimensional molecule, when the number of molecules in two dimensions is 10, the trajectory of molecular motion is:

![1](https://github.com/user-attachments/assets/5fb1ad89-b163-46f7-a6a0-6a195af4481d)


Assuming that the molecules are only subject to the force of gravity and perform parabolic motion, the trajectory of motion is:

![2](https://github.com/user-attachments/assets/ac0a41fc-63e6-4f58-90a3-cb6272cc2801)

### (2)

If the unit cell size is 1, when the coordinates of a molecule exceed the unit cell, the coordinates are shifted back into the unit cell by adding or subtracting to maintain periodic boundary conditions.Taking uniform rectilinear motion as an example:


![3](https://github.com/user-attachments/assets/e18b634b-5332-471c-8c75-d334f0e2657e)


---
