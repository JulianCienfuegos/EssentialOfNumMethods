#include <iostream>
#include <ctime>
 
using namespace std;
 
int main() {
       const int N = 4;
       const int num_iters = 100000;
       double A[N][N], a[N][N];
       double B[N][N], b[N][N];
       double C[N][N];
 
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     a[r][c] = (double)(rand() % 5);
                     b[r][c] = (double)(rand() % 5);
              }
       }
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     A[r][c] = a[r][c];
                     B[r][c] = b[r][c];
                     C[r][c] = 0;
              }
       }
       /*
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     cout << A[r][c] << " ";
              }
              cout << endl;
       }
 
 
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     cout << B[r][c] << " ";
              }
              cout << endl;
       }
       */
       clock_t start, end;
       start = clock();
       for (int iter = 0; iter < num_iters; iter++){
              for (int c = 0; c < N; c++){
                     for (int r = 0; r < N; r++){
                           for (int k = 0; k < N; k++){
                                  C[r][c] += (A[r][k] * B[k][c]);
                           }
                     }
              }
       }
       end = clock();
      
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     cout << C[r][c] << " ";
              }
              cout << endl;
       }
      
       cout << "The time taken to run this code was " << (double)(end - start)/CLOCKS_PER_SEC << endl;
 
       for (int r = 0; r < N; r++){
              for (int c = 0; c < N; c++){
                     A[r][c] = a[r][c];
                     B[r][c] = b[r][c];
                     C[r][c] = 0;
              }
       }
       start = clock();
       for (int iter = 0; iter < num_iters; iter++){
              for (int c = 0; c < N; c++){
              for (int k = 0; k < N; k++){
                           for (int r = 0; r < N; r++){
                          
                                  C[r][c] += (A[r][k] * B[k][c]);
    }}}}
  }
