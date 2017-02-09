
# leetcode 482 License Key Formatting

def licenseKeyFormatting(S, K):
	s = [x for x in S if x != '-']
	S = ''.join(s)
	k = len(S) / K
	d = len(S) % K

	ret = S[0:d]
	for i in range(k):
		s2 = S[d: d+K]
		d = d+K
		ret += '-' + s2

	if ret[0] == '-':
		ret = ret[1:]
	return ret.upper()
		

print licenseKeyFormatting('2-4A0r7-4k', 3)
