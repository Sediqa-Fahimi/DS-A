/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} p
 * @param {TreeNode} q
 * @return {boolean}
 */
// var isSameTree = function(p, q) {
//     if(p === null && q === null) return true;
//     if(p === null || q === null) return false;
//     if(p.val !== q.val) return false;
//     return isSameTree(p.right, q.right) && isSameTree(p.left, q.left);
// };
function check(p,q){
    if(p === null && q === null) return true;
    if(p === null || q === null) return false;
    if(p.val !== q.val) return false;
    return true;
}
var isSameTree = function(p, q) {
    if(p === null && q === null) return true;
    if(!check(p,q)) return false;
    
    const pq = [p];
    const qq = [q];
    let pnode,qnode;
    while(pq.length){
        pnode = pq.shift();
        qnode = qq.shift();
        
        // if(!check(pnode,qnode)) return false;
        
        if(pnode !== null){
        
            if (!check(pnode.left, qnode.left)) return false;
            if (pnode.left != null) {
              pq.push(pnode.left);
              qq.push(qnode.left);
            }
            if (!check(pnode.right, qnode.right)) return false;
            if (pnode.right != null) {
              pq.push(pnode.right);
              qq.push(qnode.right);
            }
        }
    }
    return true;
};