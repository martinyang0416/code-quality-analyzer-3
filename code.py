import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue
    L = int(line)
    if L == 0:
        break
    months = []
    for _ in range(12):
        while True:
            m_line = sys.stdin.readline()
            if not m_line:
                break
            m_line = m_line.strip()
            if m_line:
                break
        m, n = map(int, m_line.split())
        months.append((m, n))
    savings = 0
    result = 'NA'
    for i in range(12):
