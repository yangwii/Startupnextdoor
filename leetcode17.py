
# leetcode #17. Letter Combinations of a Phone Number

def letterCombinations(digits):
    def dfs(num, _str, res):
        if num == length:
            res.append(_str)
            return
        for letter in _dict[digits[num]]:
                dfs(num+1, _str+letter, res)
    
    _dict = {'2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
            }
    res = []
    length = len(digits)
    if length == 0:
        return res
    dfs(0, '', res)
    return res

def letterCombinationsv2(digits):
	chr = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
	res = []
	for i in range(0, len(digits)):
		num = int(digits[i])
		tmp = []
		for j in range(0, len(chr[num])):
			if len(res):
				for k in range(0, len(res)):
					tmp.append(res[k] + chr[num][j])
			else:
				tmp.append(str(chr[num][j]))
		res = copy.copy(tmp)

	return res

print letterCombinations('23')