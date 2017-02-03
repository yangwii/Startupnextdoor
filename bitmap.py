

# generate data
import random

# def main():
# 	numbers = random.sample(range(9999999), 9000000)

# 	open('numbers.txt', 'w').write('\n'.join(str(n) for n in numbers))


# if __name__ == '__main__':
# 	main()


# implementation

class Bitsort(object):

	def __init__(self, max_number):
		self._int_bits = 32
		self._buckets = (max_number // self._int_bits) + 1
		self._bit_array = [0] * self._buckets

	def save_number(self, number):
		bucket = number // self._int_bits
		bit_number = number % self._int_bits
		self._bit_array[bucket] |= 1 << bit_number

	def get_sort_numbers(self):
		for index, bits in enumerate(self._bit_array):
			base = index * self._int_bits

			if not bits:
				continue

			for j in range(self._int_bits):
				if bits & (1 << j):
					yield base + j


def main():
	bitsort = Bitsort(9999999)

	with open('numbers.txt', 'r') as in_file:
		for line in in_file:
			bitsort.save_number(int(line.strip()))

	out_file = open('out.txt', 'w', 4096)
	for number in bitsort.get_sort_numbers():
		out_file.write(str(number) + '\n')


if __name__ == '__main__':
	main()

