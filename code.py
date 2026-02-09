def main():
	n, k = map(int, input().split())
	a = list(map(int, input().split()))
	s = input().strip()
	last = s[0]
	seg = [a[0]]
	all = []
	for i in range(1, len(s)):
		if last == s[i]:
			seg.append(a[i])
		else:
			last = s[i]
			all.append(seg)
			seg = [a[i]]
	if seg:
		all.append(seg)
	ans = 0
	for seg in all:
		if k < len(seg):
			seg = sorted(seg, reverse = True)[:k]
		ans += sum(seg)
	print(ans)
main()