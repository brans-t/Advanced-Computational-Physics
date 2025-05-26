#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int steps = 20; // 迭代次数
    const int totalsize = 16; // 矩阵总行数
    const int mysize = 4; // 每个进程处理的列数（实际处理列数加上两列作为边界交换）
    double A[totalsize][mysize + 2]; // 主数据矩阵
    double B[totalsize][mysize + 2]; // 缓冲矩阵
    int myid, numprocs;
    int left, right;
    int tag1 = 98, tag2 = 99;
    MPI_Status status;

    // 初始化 MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);

    // 初始化矩阵 A 和 B
    for (int i = 0; i < totalsize; i++) {
        for (int j = 0; j < mysize + 2; j++) {
            A[i][j] = 0.0;
            B[i][j] = 0.0;
        }
    }
    // 设置边界条件的值
    if (myid == 0)
        for (int i = 0; i < totalsize; i++)
            A[i][1] = 8.0;
    if (myid == numprocs - 1)
        for (int i = 0; i < totalsize; i++)
            A[i][mysize] = 8.0;

    // 确定邻居
   
    left = (myid == 0) ? numprocs - 1 : myid - 1;  // 如果是进程0，则把最左边的一列设置为最后一个进程的最右边的一列
    right = (myid == numprocs - 1) ? 0 : myid + 1; // 如果是最后一个进程，则把最右边的一列设置为进程0的最左边一列
    //left = (myid > 0) ? myid - 1 : MPI_PROC_NULL;
    //right = (myid < numprocs - 1) ? myid + 1 : MPI_PROC_NULL;

    // 进行迭代计算
    for (int step = 0; step < steps; step++) {
        // 包括边界在内的发送接收，设置为周期性边界条件
        MPI_Sendrecv(&A[0][mysize], totalsize, MPI_DOUBLE, right, tag1, 
            &A[0][0], totalsize, MPI_DOUBLE, left, tag1, MPI_COMM_WORLD, &status);
        MPI_Sendrecv(&A[0][1], totalsize, MPI_DOUBLE, left, tag2,
            &A[0][mysize + 1], totalsize, MPI_DOUBLE, right, tag2, MPI_COMM_WORLD, &status);

        // 更新包括边界在内的所有矩阵元素
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                B[i][j] = (A[i][j - 1] + A[i][j + 1] + A[i - 1][j] + A[i + 1][j]) / 4.0;
            }
        }

        // 将计算结果从缓冲矩阵 B 复制回 A
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                A[i][j] = B[i][j];
            }
        }
    }

    // 打印最后的结果
    if (myid == 0) {
        printf("Final results from process %d:\n", myid);
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                printf("%.2f ", A[i][j]);
            }
            printf("\n");
        }
    }

    // 结束 MPI
    MPI_Finalize();
    return 0;
}
