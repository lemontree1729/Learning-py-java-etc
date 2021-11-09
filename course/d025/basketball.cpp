#include <bits/stdc++.h>
#include <iostream>
#include <string>
using namespace std;

int main()
{
    string a;
    getline(cin, a);
    int temp = 0, a0 = 0, b0 = 0;
    for (int i = 0; i < a.length(); i++)
    {
        if (a0 >= 11 && (a0 - b0) >= 2)
        {
            cout << "A";
            break;
        }
        if (b0 >= 11 && (b0 - a0) >= 2)
        {
            cout << "B";
            break;
        }

        if (a[i] == 'A')
        {
            temp++;
        }
        else if (a[i] == 'B')
        {
            temp--;
        }
        else
        {
            if (temp == 1)
            {
                a0 += a[i];
            }
            else
            {
                b0 += a[i];
            }
            temp = 0;
        }
    }
    return 0;
}