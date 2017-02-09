
# leetcode 388 Longest Absolute File Path


def lengthLongestPath(input):
	maxlen = 0
	pathlen = {0: 0}

	for line in input.splitlines():
		name = line.lstrip('\t')
		depth = len(line) - len(name)

		if '.' in name:
			maxlen = max(maxlen, pathlen[depth] + len(name)) # file.txt so not add + 1 as below line
		else:
			pathlen[depth + 1] = pathlen[depth] + len(name) + 1

	return maxlen


print lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext")
