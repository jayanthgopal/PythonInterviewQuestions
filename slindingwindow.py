def countDistinct(arr, k, n):
    print(arr)
    for i in range(0, n-k+1):
        s = set()
        for j in range(i, i+k):
            print(arr[j])
            s.add(arr[j])

        print("--{}---".format(len(s)))
    return


arr = [1, 2, 1, 3, 4, 2, 3]
n = len(arr)
k = 4
countDistinct(arr, k, n)
