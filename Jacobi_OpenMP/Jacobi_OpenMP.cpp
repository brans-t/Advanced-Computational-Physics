#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

#define TOTALSIZE 16
#define MYSIZE 4
#define STEPS 20

int main() {
    double A[TOTALSIZE][MYSIZE + 2] = { 0 };  // �����ݾ��󣬰����߽���
    double B[TOTALSIZE][MYSIZE + 2] = { 0 };  // ���ڵ�������Ļ������
    int i, j, step;

    // ��ʼ���߽�����
    // �������ǳ�ʼ���߽�Ϊĳ���̶�ֵ������ 1.0
    for (i = 0; i < TOTALSIZE; i++) {
        A[i][0] = 8.0;  // ��߽�
        A[i][MYSIZE + 1] = 8.0;  // �ұ߽�
    }

    // ���� Jacobi ����
    for (step = 0; step < STEPS; step++) {
#pragma omp parallel for private(j) shared(A, B)
        for (i = 1; i < TOTALSIZE - 1; i++) {
            for (j = 1; j <= MYSIZE; j++) {
                B[i][j] = 0.25 * (A[i][j - 1] + A[i][j + 1] + A[i - 1][j] + A[i + 1][j]);
            }
        }

        // ���¼�������ݸ��ƻ� A
#pragma omp parallel for private(j) shared(A, B)
        for (i = 1; i < TOTALSIZE - 1; i++) {
            for (j = 1; j <= MYSIZE; j++) {
                A[i][j] = B[i][j];
            }
        }
    }

    // ��ӡ���
    if (omp_get_thread_num() == 0) {  // ȷ��ֻ��һ���̣߳����̣߳�ִ�д�ӡ����
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
