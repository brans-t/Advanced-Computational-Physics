#include "mpi.h"
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char* argv[]) {
    int steps = 20; // ��������
    const int totalsize = 16; // ����������
    const int mysize = 4; // ÿ�����̴����������ʵ�ʴ�����������������Ϊ�߽罻����
    double A[totalsize][mysize + 2]; // �����ݾ���
    double B[totalsize][mysize + 2]; // �������
    int myid, numprocs;
    int left, right;
    int tag1 = 98, tag2 = 99;
    MPI_Status status;

    // ��ʼ�� MPI
    MPI_Init(&argc, &argv);
    MPI_Comm_rank(MPI_COMM_WORLD, &myid);
    MPI_Comm_size(MPI_COMM_WORLD, &numprocs);

    // ��ʼ������ A �� B
    for (int i = 0; i < totalsize; i++) {
        for (int j = 0; j < mysize + 2; j++) {
            A[i][j] = 0.0;
            B[i][j] = 0.0;
        }
    }
    // ���ñ߽�������ֵ
    if (myid == 0)
        for (int i = 0; i < totalsize; i++)
            A[i][1] = 8.0;
    if (myid == numprocs - 1)
        for (int i = 0; i < totalsize; i++)
            A[i][mysize] = 8.0;

    // ȷ���ھ�
   
    left = (myid == 0) ? numprocs - 1 : myid - 1;  // ����ǽ���0���������ߵ�һ������Ϊ���һ�����̵����ұߵ�һ��
    right = (myid == numprocs - 1) ? 0 : myid + 1; // ��������һ�����̣�������ұߵ�һ������Ϊ����0�������һ��
    //left = (myid > 0) ? myid - 1 : MPI_PROC_NULL;
    //right = (myid < numprocs - 1) ? myid + 1 : MPI_PROC_NULL;

    // ���е�������
    for (int step = 0; step < steps; step++) {
        // �����߽����ڵķ��ͽ��գ�����Ϊ�����Ա߽�����
        MPI_Sendrecv(&A[0][mysize], totalsize, MPI_DOUBLE, right, tag1, 
            &A[0][0], totalsize, MPI_DOUBLE, left, tag1, MPI_COMM_WORLD, &status);
        MPI_Sendrecv(&A[0][1], totalsize, MPI_DOUBLE, left, tag2,
            &A[0][mysize + 1], totalsize, MPI_DOUBLE, right, tag2, MPI_COMM_WORLD, &status);

        // ���°����߽����ڵ����о���Ԫ��
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                B[i][j] = (A[i][j - 1] + A[i][j + 1] + A[i - 1][j] + A[i + 1][j]) / 4.0;
            }
        }

        // ���������ӻ������ B ���ƻ� A
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                A[i][j] = B[i][j];
            }
        }
    }

    // ��ӡ���Ľ��
    if (myid == 0) {
        printf("Final results from process %d:\n", myid);
        for (int i = 1; i < totalsize - 1; i++) {
            for (int j = 1; j <= mysize; j++) {
                printf("%.2f ", A[i][j]);
            }
            printf("\n");
        }
    }

    // ���� MPI
    MPI_Finalize();
    return 0;
}
