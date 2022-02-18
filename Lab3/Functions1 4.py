def prime(n):
    for i in range(3, n):
        if n % i == 0:
            return False
    return True
def filter_prime(a):
    for i in a:
        if prime(i) == True:
            print(i,end=' ')
arr = list(map(int,input().split()))
filter_prime(arr)