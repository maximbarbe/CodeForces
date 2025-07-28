#include <bits/stdc++.h>
using namespace std;


#define all(x) begin(x), end(x);

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;
const double PI = acos(-1);

class TreeNode {

    public:

        int val;
        TreeNode *left = nullptr;
        TreeNode *right = nullptr;

        TreeNode(int val, TreeNode *left, TreeNode *right) {
            this -> left = left;
            this -> right = right;
            this -> val = val;
        }
};

class Tree {
    public:
        static TreeNode* buildTree(vi &arr) {
            vector<TreeNode*> nextLevel;
            bool o = true;
            for (auto v:arr) {
                nextLevel.push_back(new TreeNode(v, nullptr, nullptr));
            }
            
            while (nextLevel.size() != 1) {
                vector<TreeNode*> newArr = nextLevel;
                nextLevel = vector<TreeNode*>();
                for (int i = 0; i < newArr.size(); i += 2) {
                    TreeNode* left = newArr[i];
                    TreeNode* right = newArr[i + 1];
                    if (o) {
                        nextLevel.push_back(new TreeNode(left->val | right->val, left, right));
                    } else {
                        nextLevel.push_back(new TreeNode(left->val ^ right->val, left, right));
                    }

                }
                o ^= true;
            }


            return nextLevel[0];
        }

        static int updateTree(TreeNode *root, int left, int right, int idx, int val) {
            if (left == right) {
                root -> val = val;
                return 0;
            } else {
                int mid = left + (right-left)/2;
                int height;
                if (idx <= mid) {
                    height = updateTree(root -> left, left, mid, idx, val);
                } else {
                    height = updateTree(root -> right, mid + 1, right, idx, val);
                }
                if (height % 2 == 0) {
                    root -> val = root -> left -> val | root -> right -> val;
                } else {
                    root -> val = root -> left -> val ^ root -> right -> val;
                }
                return height + 1;
            }
        }
        
};


int main() {
    ios::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int n, m, v, p, b;
    
    cin >> n >> m;
    n = (int)pow(2, n);
    vi vals;
    for (int i = 0; i < n; i++) {
        cin >> v;
        vals.push_back(v);
    }
    
    TreeNode* root = Tree::buildTree(vals);
    for (int i = 0; i < m; i++) {
        cin >> p >> b;
        p --;
        Tree::updateTree(root, 0, n-1, p, b);
        cout << root -> val << endl;
    }




}