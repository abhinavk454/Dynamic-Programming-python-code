def subset(arr, k):
    if sum(arr) == k:
        return True
    if not arr:
        return False
    elif arr[-1] <= k:
        return (subset(arr[:-1], k-arr[-1])) or (subset(arr[:-1], k))
    elif arr[-1] > k:
        return subset(arr[:-1], k)


print(subset([1, 2, 3], 4))
