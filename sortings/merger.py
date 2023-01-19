def merger(A, B, lenA, lenB):
    i = lenA - 1
    j = lenB - 1
    k = lenA + lenB - 1
    while k >= 0:
        if i < 0:
            A[k] = B[j]
            j -= 1
        elif j < 0:
            break
        elif A[i] > B[j]:
            A[k] = A[i]
            i -= 1
        else:
            A[k] = B[j]
            j -= 1
        k -= 1

