
#leetcode 6 zigzag

def convert(s, numRows):
	if len(s) == 0 or len(s) <= numRows or numRows == 1:
		return s
	lists = []
	for i in range(numRows):
		lists.append('')
	direction = 0
	i = 0
	for ch in s:
		if direction == 0:
			lists[i] += ch
			i += 1
		else:
			lists[i] += ch
			i = i - 1

		if i + 1 == numRows:
			direction = -1
		elif i == 0 and direction == -1:
			direction = 0

	return ''.join(lists)


print convert('ABC', 2)