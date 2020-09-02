"""
 BottomUp Dp
 Each recursive call of subtree is returning a answer to top part of tree,
 it means that we are building the tree from bottom to top and the answers computed at the bottom are passsed to the top,
 Anyways it its not stored in seperate table  since those temp and res are themselves getting updated in each call.
"""

class Solution:
    def __init__(self):
        self.res=-1
    def main(self):
        def soln(root):
            if not root:
                return 0
            lc, rc = None, None
            if root.left:
                lc = soln(root.left)
            if root.right:
                rc = soln(root.right)
            temp = max(lc, rc)+1  # if it passes to upper node
            ans = max(temp, 1+lc+rc)
            self.res = max(self.res, ans)
            return temp
