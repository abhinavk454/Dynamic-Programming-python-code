def knapsack(wt, val, w, n):
    # it is the base case if bag is full of wt in none then we can get maximum 0 profit
    if n == 0 or w == 0:
        return 0
    # below case handles if weight of last element is less than the bags weight
    if wt[-1] <= w:
        # contains two choices weather to include or mot include these items
        # so we will return which gives maximum weather case 1 or case 2
        return max((val[-1]+knapsack(wt[:-1], val[:-1], w-wt[-1], n-1)), knapsack(wt[:-1], val[:-1], w, n-1))
    elif wt[-1] > w:
        return knapsack(wt[:-1], val[:-1], w, n-1)


print(knapsack([1, 3, 4, 5], [1, 4, 5, 7], 7, 4))
