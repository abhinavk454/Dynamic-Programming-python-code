import sys


def soln(e, f):
    if f <= 1:
        return f
    if e <= 1:  # we calculating the wrost case so we may have to go upto f floor
        return f
    min_ans = 9999999999
    for k in range(1, f+1):  # will go upto last floor
        # 1 for ground floor since its base and max for worst case
        # print(f-k)
        min_temp = 1 + max(soln(e-1, k-1), soln(e, f-k))
        min_ans = min(min_ans, min_temp)
    return min_ans


# def eggDrop(n, k):

#     # If there are no floors, then no trials
#     # needed. OR if there is one floor, one
#     # trial needed.
#     if (k == 1 or k == 0):
#         return k

#     # We need k trials for one egg
#     # and k floors
#     if (n == 1):
#         return k

#     min = sys.maxsize

#     # Consider all droppings from 1st
#     # floor to kth floor and return
#     # the minimum of these values plus 1.
#     for x in range(1, k + 1):

#         res = max(eggDrop(n - 1, x - 1),
#                   eggDrop(n, k - x))
#         if (res < min):
#             min = res

#     return min + 1


print(soln(2, 10))
