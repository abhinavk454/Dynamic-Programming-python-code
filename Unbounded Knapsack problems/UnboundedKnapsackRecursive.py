def soln(wt, val, w, n):
    if n == 0 or w == 0:
        return 0

    elif wt[-1] <= w:
        return max(val[-1]+soln(wt, val, w-wt[-1], n-1), soln(wt[:-1], val[:-1], w, n-1))
    elif wt[-1] > w:
        return soln(wt[:-1], val[:-1], w, n-1)


print(soln([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
