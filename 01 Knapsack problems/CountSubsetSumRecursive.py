def count(arr, k):
    if not arr:
        return 0
    if sum(arr) == k:
        return 1
    elif arr[-1] <= k:
        return count(arr[:-1], k-arr[-1])+count(arr[:-1], k)
    elif arr[-1] > k:
        return count(arr[:-1], k)


print(count([1, 2, 3, 4, 5], 6))
