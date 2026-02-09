n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

error1 = sum(a) - sum(b)
error2 = sum(b) - sum(c)

print(error1)
print(error2)