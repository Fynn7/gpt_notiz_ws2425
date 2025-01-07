import sys

text = []
path = sys.argv[1]
with open(path, "r",encoding="utf-8") as file:
	text = file.readlines()
lines_number=len(text)

for line_index in range(lines_number-1, -1, -1):
	line_length = len(text[line_index])
	for char_index in range(line_length-1, -1, -1):
		sys.stdout.write(text[line_index][char_index])
		print(text[line_index][char_index], end="")