"""
 BottomUp Dp
 Each recursive call of subtree is returning a answer to top part of tree,
 it means that we are building the tree from bottom to top and the answers computed at the bottom are passsed to the top,
 Anyways it its not stored in seperate table  since those temp and res are themselves getting updated in each call.
"""


class Solution:
    def __init__(self):
        self.res = -1

    def main(self):
        def soln(root):
            if not root:
                return 0
            lc, rc = None, None
            if root.left:
                lc = soln(root.left)
            if root.right:
                rc = soln(root.right)
            # second case is for if both rchild of tree return negative sum
            # if it passes to upper node
            temp = max(max(lc, rc)+root.val, root.val)
            # if root dosent wnat to pass value to its parent
            ans = max(temp, root.val+lc+rc)
            self.res = max(self.res, ans)
            return temp
