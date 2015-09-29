from random import randint

def puzzle1_builder(size, target, top, high_div):
	print "Are you sure?",
	raw_input()
	file = open("puzzle1_input.txt", "w+")
	file.write(str(target) + "\n")

	for i in range(0, size):
		file.write(str(randint(0, top)) + "\n")

	file.close()

if __name__ == "__main__":
	num = 10
	puzzle1_builder(500, 2000, num, num)