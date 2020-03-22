def issubset(arr1, arr2):
    ar1_dict = {}
    for i in arr1:
        ar1_dict[i] = True

    for j in arr2:
        try:
            if ar1_dict[j]:
                continue
        except Exception as e:
            return False

    return True


# Driver code
if __name__ == "__main__":

    arr1 = [11, 1, 13, 21, 3, 7]
    arr2 = [11, 3, 22, 1]

    m = len(arr1)
    n = len(arr2)

    if issubset(arr1, arr2):
        print("arr2[] is subset of arr1[] ")
    else:
        print("arr2[] is not a subset of arr1[]")