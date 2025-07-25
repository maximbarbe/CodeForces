#include <cstdio>
#include <vector>
#include <algorithm>
#include <iostream>
#include <iomanip>
#include <set>
#include <string>
#include <tuple>
#include <math.h>
#include <map>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);

map<int, vi> edges;


double dfs(int prev, int src) {
    double cur = 0.0;
    for (auto dest:edges[src]) {
        if (dest != prev) {
            cur += dfs(src, dest);
        }
    }
    if (cur == 0) {
        return 1;
    } else if (src != 1) {
        return 1 + cur/(edges[src].size() - 1);
    } else {
        return 1 + cur/(edges[src].size());
    }


}




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, x, y;
    cin >> n;
    for (int i = 0; i < n - 1; i++) {
        cin >> x >> y;
        edges[x].push_back(y);
        edges[y].push_back(x);
    }
    cout << setprecision(8);
    cout << dfs(0, 1) - (double)1.0 << endl;


}