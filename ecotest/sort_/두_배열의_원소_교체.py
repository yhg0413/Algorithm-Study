




def sol(n,k,A,B):

    for i in range(k):
        min_A = A[i]
        max_B = B[i]
        for j in range(i+1,n):
            if min_A > A[j]:
                min_A = A[j]
                A[i], A[j] = min_A, A[i]
            if max_B < B[j]:
                max_B = B[j]
                B[i], B[j] = max_B, B[i]

        A[i],B[i] = B[i], A[i]

    print(A,B)

    return sum(A)

def sol2(n,k,A,B):
    A.sort()
    B.sort(reverse=True)

    for i in range(k):
        if A[i] < B[i]:
            A[i], B[i] = B[i], A[i]
        else:
            break
    print(sum(A))

if __name__ == '__main__':
    print(sol(5,3,[1,2,5,4,3],[5,5,6,6,5]))


