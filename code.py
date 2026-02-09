import sys

def main():
    input = sys.stdin.read
    data = input().split()
    T = int(data[0])
    index = 1
    for _ in range(T):
        a = int(data[index])
        b = int(data[index+1])
        c = int(data[index+2])
        index += 3
        k = (c - b) // a
        x = k * a + b
        print(x)
        
if __name__ == "__main__":
    main()