a = "abcdefghijklmnopqrstuvwxyz"
def alpha (r,n):
    if len(r)==1 and r[0]==n:
        print("YES")
        return 0
    elif r[0]==n:
        alpha(r[1:],a[(a.find(n))-1])
    elif r[-1]==n:
         alpha(r[:-1],a[(a.find(n))-1])
    else:
        print("NO")
k = int(input())
for i in range(k):
    r = str(input())
    alpha(r,a[len(r)-1])