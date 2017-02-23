
#leetcode 401. Binary Watch

def readBinaryWatch(num):
	ans = []
	hour = [[], [], [], []]
	minte = [[], [], [], [], [], []]

	for i in range(0, 12):
		n = bin(i).count('1')
		hour[n].append(i)
	for i in range(0, 60):
		n = bin(i).count('1')
		minte[n].append(i)

	for i in range(0, num + 1):
		if i < 4 and num - i < 6:
			for h in hour[i]:
				for m in minte[num - i]:
					ans.append('%d:%02d' % (h, m))
	return ans

print readBinaryWatch(2)