import sys

class State:
    __slots__ = ['len', 'link', 'next']
    def __init__(self):
        self.len = 0
        self.link = -1
        self.next = dict()

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    cases = input[1:T+1]
    for s in cases:
        sa = [State()]
        sa[0].link = -1
        sa[0].len = 0
        last = 0
        size = 1
        cnt = [0]
        for c in s:
            p = last
            curr = size
            sa.append(State())
      