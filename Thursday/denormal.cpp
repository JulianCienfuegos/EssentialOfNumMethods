#include <ctime>
#include <iostream>

using namespace std;

clock_t start, end;

int main(){
    const double x[16] = {  1.1,   1.2,   1.3,     1.4,   1.5,   1.6,   1.7,   1.8,
                           1.9,   2.0,   2.1,     2.2,   2.3,   2.4,   2.5,   2.6};
    const double z[16] = {1.123, 1.234, 1.345, 156.467, 1.578, 1.689, 1.790, 1.812,
                         1.923, 2.034, 2.145,   2.256, 2.367, 2.478, 2.589, 2.690};
    double y[16];
    for (int i = 0; i < 16; i++)
    {
        y[i] = x[i];
    }

    start = clock();
    for (int j = 0; j < 9000000; j++)
    {
        for (int i = 0; i < 16; i++)
        {
            y[i] *= x[i];
            y[i] /= z[i];
            y[i] = y[i] + 0.1; // <--
            y[i] = y[i] - 0.1; // <--
        }
    }
    end = clock();

    cout << "The run time with normal numbers is " << (double)(end - start)/CLOCKS_PER_SEC << endl;
    cout << "y is: " << endl;
    for(int i = 0; i < 16; i++){
        cout << y[i] << " ";
    }
    cout << endl;

    for (int i = 0; i < 16; i++)
    {
        y[i] = x[i];
    }

    start = clock();
    for (int j = 0; j < 9000000; j++)
    {
        for (int i = 0; i < 16; i++)
        {
            y[i] *= x[i];
            y[i] /= z[i];
            y[i] = y[i] + 0; // <--
            y[i] = y[i] - 0; // <--
        }
    }
    end = clock();

    cout << "The run time with denormal numbers is " << (double)(end - start)/CLOCKS_PER_SEC << endl;
    cout << "y is: " << endl;
    for(int i = 0; i < 16; i++){
        cout << y[i] << " ";
    }
    cout << endl;

}