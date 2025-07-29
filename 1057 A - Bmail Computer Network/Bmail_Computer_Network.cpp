#include <bits/stdc++.h>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);


map<int, vi> edges;
map<int, bool> visited;



void dfs(int cur, int n, vi &path) {
    if (cur == n-1) {
        for (int i = 0; i < path.size() - 1; i++) {
            cout << path[i] + 1 << " ";
        }
        cout << path[path.size() - 1] + 1 << endl;
        exit(0);
    }
    for (auto dest:edges[cur]) {
        if (!visited[dest]) {
            visited[dest] = true;
            path.push_back(dest);
            dfs(dest, n, path);
            path.pop_back();
            visited[dest] = false;
        }
    }
}




int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, u, v;
    cin >> n;
    for (int i = 0; i < n-1; i++) {
        u = i+1;
        cin >> v;
        v -= 1;
        if (u != v) {
            edges[u].push_back(v);
            edges[v].push_back(u);
        }
    }
    vi path = {0};
    visited[0] = true;
    dfs(0, n, path);




}