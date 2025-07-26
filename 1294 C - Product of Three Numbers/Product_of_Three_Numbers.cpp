#include <bits/stdc++.h>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);

map<int, vi> edges;



void res(int n) {
    if (n < 24) {
        cout << "NO" << endl;
        return;
    }
    
    for (int a = 2; a <= floor(pow(n, 1/3.0)); a++) {
        if (n%a == 0) {
            int temp = n/a;
            for (int b = a + 1; b <= floor(pow(temp, 1/2.0)); b++) {
                if (temp % b == 0 && temp/b != b && temp/b != a) {
                    cout << "YES" << endl;
                    cout << a << " " << b << " " << temp/b<<endl;
                    return;
                }
            }
        }
    }
    cout << "NO" << endl;
    return;
} 


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int t, n;
    cin >> t;

    for (int i = 0; i < t; i++) {
        cin >> n;
        res(n);
    }



}