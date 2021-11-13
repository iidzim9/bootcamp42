//? harshad number 
//? 12345 -> 1 + 2 + 3 + 4 + 5 = 15
//? 12345 / 15 = 823 -> True

//! 3216 -> 3 + 2 + 1 + 6 + 1 = 13
//! 32161 / 13

#include <iostream>
#include <string>
#include <cmath>
using namespace std;

int main(void)
{
    int n;
    cout << "enter an integer > ";
    cin >> n;
    string s = to_string(n);
    int sum = 0;
    for (int i = 0; i < s.size(); i++)
        sum += s[i] - '0';
    float val = n / sum;
    if (floor(val) == (n / sum))
        cout << "true" << endl;
    else
        cout << "false" << endl;
    return (0);
}

