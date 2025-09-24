Complexity Analysis
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: list[int]) -> list[TreeNode]:
        res: dict[int, TreeNode] = {root.val: root}
        to_delete: set[int] = set(to_delete)

        def recursion(parent: TreeNode | None, cur_node: TreeNode | None, isleft: bool) -> None:
            nonlocal res
            if cur_node is None:
                return

            recursion(cur_node, cur_node.left, True)
            recursion(cur_node, cur_node.right, False)

            if cur_node.val in to_delete:
                if cur_node.val in res:
                    del res[cur_node.val]

                if parent:
                    if isleft:
                        parent.left = None
                    else:
                        parent.right = None

                if cur_node.left:
                    res[cur_node.left.val] = cur_node.left
                if cur_node.right:
                    res[cur_node.right.val] = cur_node.right

        recursion(None, root, False)
        return res.values()



#in cpp

class Solution {
public:
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        unordered_map<int, TreeNode*> res;
        unordered_set<int> to_delete_set(to_delete.begin(), to_delete.end());
        res[root->val] = root;

        function<void(TreeNode*, TreeNode*, bool)> recursion = [&](TreeNode* parent, TreeNode* cur_node, bool isleft) {
            if (cur_node == nullptr) return;

            recursion(cur_node, cur_node->left, true);
            recursion(cur_node, cur_node->right, false);

            if (to_delete_set.find(cur_node->val) != to_delete_set.end()) {
                if (res.find(cur_node->val) != res.end()) {
                    res.erase(cur_node->val);
                }

                if (parent) {
                    if (isleft) {
                        parent->left = nullptr;
                    } else {
                        parent->right = nullptr;
                    }
                }

                if (cur_node->left) {
                    res[cur_node->left->val] = cur_node->left;
                }
                if (cur_node->right) {
                    res[cur_node->right->val] = cur_node->right;
                }
            }
        };

        recursion(nullptr, root, false);
        
        vector<TreeNode*> result;
        for (auto& pair : res) {
            result.push_back(pair.second);
        }
        
        return result;
    }
};


#in java

class Solution {
    public List<TreeNode> delNodes(TreeNode root, int[] to_delete) {
        Map<Integer, TreeNode> res = new HashMap<>();
        Set<Integer> to_delete_set = new HashSet<>();
        for (int val : to_delete) {
            to_delete_set.add(val);
        }
        res.put(root.val, root);

        recursion(null, root, false, res, to_delete_set);

        return new ArrayList<>(res.values());
    }

    private void recursion(TreeNode parent, TreeNode cur_node, boolean isleft, Map<Integer, TreeNode> res, Set<Integer> to_delete_set) {
        if (cur_node == null) return;

        recursion(cur_node, cur_node.left, true, res, to_delete_set);
        recursion(cur_node, cur_node.right, false, res, to_delete_set);

        if (to_delete_set.contains(cur_node.val)) {
            res.remove(cur_node.val);

            if (parent != null) {
                if (isleft) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            }

            if (cur_node.left != null) {
                res.put(cur_node.left.val, cur_node.left);
            }
            if (cur_node.right != null) {
                res.put(cur_node.right.val, cur_node.right);
            }
        }
    }
}



#in js
var delNodes = function(root, to_delete) {
    let res = {};
    let to_delete_set = new Set(to_delete);
    res[root.val] = root;

    function recursion(parent, cur_node, isleft) {
        if (cur_node === null) return;

        recursion(cur_node, cur_node.left, true);
        recursion(cur_node, cur_node.right, false);

        if (to_delete_set.has(cur_node.val)) {
            delete res[cur_node.val];

            if (parent !== null) {
                if (isleft) {
                    parent.left = null;
                } else {
                    parent.right = null;
                }
            }

            if (cur_node.left !== null) {
                res[cur_node.left.val] = cur_node.left;
            }
            if (cur_node.right !== null) {
                res[cur_node.right.val] = cur_node.right;
            }
        }
    }

    recursion(null, root, false);

    return Object.values(res);
};
