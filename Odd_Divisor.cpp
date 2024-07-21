

#pragma GCC optimize("Ofast") 
#pragma GCC target("avx,avx2,fma")



#include <iostream>
#include <iomanip>
#include <vector>
#include <tuple>
#include <algorithm>
#include <math.h>
#include <string>
#include <queue>
#include <string>
#include <unordered_map>
typedef long long ll;



using namespace std;







int main() {
    int t;
    ll n;
    cin >> t;
    for (int i = 0; i < t;i ++) {
        cin >> n;
        while (n % 2 == 0) {
            n/=2;
        }
        if (n ==1) {
            cout << "NO" << endl;
        } else {
            cout << "YES" << endl;
        }
    }

}