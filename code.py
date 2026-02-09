def main():
    n, x, y = map(int, input().split())
    number = list(input())
    count = 0
    i = 0
    while i < y:
        if number[-i - 1] != '0':
            count += 1
            number[-i - 1] = '0'
        i += 1
    i += 1
    if number[-y - 1] == "0":
        number[-y -1] = "1"
        count += 1
    while i < x:
        if number[-i - 1] != '0':
            count += 1
            number[-i - 1] = '0'
        i += 1
    print(count)



main()
