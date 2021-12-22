//? harshad number 
//? 12345 -> 1 + 2 + 3 + 4 + 5 = 15
//? 12345 / 15 = 823 -> True

//! 3216 -> 3 + 2 + 1 + 6 + 1 = 13
//! 32161 / 13

// #include <iostream>
// #include <string>
// #include <cmath>
// using namespace std;

// int main(void)
// {
//     int n;
//     cout << "enter an integer > ";
//     cin >> n;
//     string s = to_string(n);
//     int sum = 0;
//     for (int i = 0; i < s.size(); i++)
//         sum += s[i] - '0';
//     float val = n / sum;
//     if (floor(val) == (n / sum))
//         cout << "true" << endl;
//     else
//         cout << "false" << endl;
//     return (0);
// }


// x,y=map(int,open(0))
// print((x+y)*min(x,y))


// int main()
// {
//     int x;
//     cin >> x; cin.ignore();
//     int y;
//     cin >> y; cin.ignore();

//     if (x > y)
//         cout << y * (x + y) << endl;
//     else
//         cout << x * (x + y) << endl;
// }



// int frq[555];

// int main()
// {
//     string s;
//     getline(cin, s);

//     for(int i=0 ; i<s.size() ; i++){
//         char x=tolower(s[i]);
//         frq[x]++;
//     }

//     bool f=0;
//     for(int i=0 ; i<s.size() ; i++){
//         char x=tolower(s[i]);
//         if(x != ' '){
//             if(frq[x]){
//                 if(f) cout<<" ";
//                 cout<<x<<":"<<frq[x];
//                 f=1;
//                 frq[x]=0;
//             }
//         }
//     }
    
// }


int main()
{
    int n;
    cin >> n; cin.ignore();
    for (int i = 0; i < n; i++) {
        int a;
        int b;
        cin >> a >> b; cin.ignore();
        int min = std::min(abs(a-b), abs(100+a-b), abs(100+b-a));
        cout << min << endl;
    }
}