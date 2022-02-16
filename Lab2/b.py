n = int(input())
arr = list(map(int, input().split()))
arr.sort()
a = arr[n-1]
b = arr[n-2]
print(a*b)