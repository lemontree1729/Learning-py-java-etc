#include <iostream>
using namespace std;

int main(void)
{
    int *a = nullptr; // declare pointer and initialize it
                      // so that it doesn't store a random address
    int i = 5;
    a = &i;     // assign pointer to address of object
    int j = *a; // dereference a to retrieve the value at its address
    cout << a << endl
         << i << endl
         << j;
    return 0;
}