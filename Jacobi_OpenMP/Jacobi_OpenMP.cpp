#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define TOTALSIZE 16
#define MYSIZE 4
#define STEPS 20

int main() {
    double A[TOTALSIZE][MYSIZE + 2] = { 0 };  // 主数据矩阵，包含边界列
    double B[TOTALSIZE][MYSIZE + 2] = { 0 };  // 用于迭代计算的缓冲矩阵
    int i, j, step;

    // 初始化边界条件
    // 假设我们初始化边界为某个固定值，例如 1.0
    for (i = 0; i < TOTALSIZE; i++) {
        A[i][0] = 8.0;  // 左边界
        A[i][MYSIZE + 1] = 8.0;  // 右边界
    }

    // 进行 Jacobi 迭代
    for (step = 0; step < STEPS; step++) {
#pragma omp parallel for private(j) shared(A, B)
        for (i = 1; i < TOTALSIZE - 1; i++) {
            for (j = 1; j <= MYSIZE; j++) {
                B[i][j] = 0.25 * (A[i][j - 1] + A[i][j + 1] + A[i - 1][j] + A[i + 1][j]);
            }
        }

        // 将新计算的数据复制回 A
#pragma omp parallel for private(j) shared(A, B)
        for (i = 1; i < TOTALSIZE - 1; i++) {
            for (j = 1; j <= MYSIZE; j++) {
                A[i][j] = B[i][j];
            }
        }
    }

    // 打印结果
    if (omp_get_thread_num() == 0) {  // 确保只有一个线程（主线程）执行打印操作
        printf("Final results:\n");
        for (i = 1; i < TOTALSIZE - 1; i++) {
            for (j = 1; j <= MYSIZE; j++) {
                printf("%.2f ", A[i][j]);
            }
            printf("\n");
        }
    }

    return 0;
}
