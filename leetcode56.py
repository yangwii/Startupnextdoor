
# leetcode #56 Merge Intervals

class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __str__(self):
     	return '[%d, %d]' % (self.start, self.end)

def merge(intervals):
	intervals = sorted(intervals, key=lambda x:x.start, reverse=True)
	res = []
	while True:
		if len(intervals) == 1:
			res.append(intervals[0])
			break
		j = intervals.pop()
		if intervals[len(intervals) - 1].start <= j.end <= intervals[len(intervals) - 1].end:
			tmp = Interval(j.start, intervals[len(intervals) - 1].end)
			intervals.pop()
			intervals.append(tmp)
		elif intervals[len(intervals) - 1].end <= j.end:
			intervals.pop()
			intervals.append(j)
		else:
			res.append(j)
		
	for re in res:
		print re

l = [Interval(1, 34), Interval(2, 6), Interval(15, 18), Interval(8, 10)]
merge(l)