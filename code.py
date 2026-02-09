n = int(input())
list1 = list(map(int, input().split()))
s1 = set(list1)
list2 = list(map(int, input().split()))
s2 = set(list2)
list3 = list(map(int, input().split()))
s3 = set(list3)

fixed1 = (s1 - s2).pop()
fixed2 = (s2 - s3).pop()

print(fixed1)
print(fixed2)