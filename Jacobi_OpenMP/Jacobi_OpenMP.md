- Use the OpenMP method to parallelize the Jacobi iteration program.

- Test the Pi calculation program (calc_pi_omp-bug.c). When the loop variable private(i) attribute is not set, the results may be incorrect on some systems when num_steps is large. Try multiple times and compare the impact of having or not having private(i) on the results.