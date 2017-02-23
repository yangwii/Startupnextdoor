
# leetcode 60. Permutation Sequence

'''
在n!个排列中，第一位的元素总是(n-1)!一组出现的，也就说如果p = k / (n-1)!，那么排列的最开始一个元素一定是nums[p]。

假设有n个元素，第K个permutation是
a1, a2, a3, .....   ..., an
那么a1是哪一个数字呢？
那么这里，我们把a1去掉，那么剩下的permutation为
a2, a3, .... .... an, 共计n-1个元素。 n-1个元素共有(n-1)!组排列，那么这里就可以知道
设变量K1 = K
a1 = K1 / (n-1)!
同理，a2的值可以推导为
a2 = K2 / (n-2)!
K2 = K1 % (n-1)!
 .......
a(n-1) = K(n-1) / 1!
K(n-1) = K(n-2) /2!
an = K(n-1)
'''

def getPermutation(n, k):
	fac = [1]
	for i in range(1, n + 1):
		fac.append(fac[-1] * i)

	elegible = range(1, n + 1)
	per = []
	for i in range(n):
		digit = (k - 1) / fac[n - i - 1]
		per.append(elegible[digit])
		elegible.remove(elegible[digit])
		k = (k - 1) % fac[n - i - 1] + 1

	return ''.join([str(x) for x in per])