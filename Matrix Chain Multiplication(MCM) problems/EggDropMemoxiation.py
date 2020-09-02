def Solve(eggs, floors):
    # Initialize T with 0's
    T = [[0 for _ in range(floors+1)] for _ in range(eggs+1)]
    # If only 1 egg was given
    for j in range(floors+1):
        T[1][j] = j
    for i in range(2, eggs+1):  # From 2 because we do not want to overwrite row index 1 values
        for j in range(1, floors+1):
            T[i][j] = float('inf')
            for k in range(1, j+1):
                count = 1 + max(T[i-1][k-1], T[i][j-k])
                T[i][j] = min(T[i][j], count)
    return T[i][j]


eggs = 2
floors = 100
attempts = Solve(eggs, floors)
print('Min # of attempts: ', attempts)
