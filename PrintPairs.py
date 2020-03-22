def printPairs(A, len, n):
    s = set()
    for i in range(0, len):
        temp = n - A[i]
        if temp in A:
            print("{} and {}".format(A[i], temp))
        s.add(A[i])

    return

# driver program to check the above function
A = [1, 4, 45, 6, 10, 8]
n = 16
printPairs(A, len(A), n)