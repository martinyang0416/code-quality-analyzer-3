n = int(input())
a_list = list(map(int, input().split()))
m = int(input())
b_list = list(map(int, input().split()))

max_ratio = 0
count = 0

for a in a_list:
    for b in b_list:
        if b % a == 0:
            ratio = b // a
            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1

print(count)