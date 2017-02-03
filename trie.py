

class TrieNode:
	__slots__ = ['letters', 'word_count', 'ends_word']
	
	def __init__(self):
		self.letters = {}
		self.word_count = 0
		self.ends_word = False
		

class Contacts:
	def __init__(self):
		self.root = TrieNode()
		
	def add(self, word):
		current = self.root
		for ch in word:
			current.word_count += 1
			# if ch not in current.letters:
			# 	current.letters[ch] = TrieNode()
			# current = current.letters[ch]
			current = current.letters.setdefault(ch, TrieNode()) # better than up 3 lines
			
		current.word_count += 1
		current.ends_word = True
		
	def partial(self, prefix):
		current = self.root
		if ch in prefix:
			if ch in current.letters:
				current = current.letters[ch]
			else:
				return 0
				
		return current.word_count

	def contains(self, word):
		current = self.root
		for ch in word:
			if ch in current.letters:
				current = current.letters[ch]
			else:
				return False

		return True


if __name__ == '__main__':
	obj = Contacts()
	obj.add('word')
	if obj.contains('word'):
		print 'easy'
	