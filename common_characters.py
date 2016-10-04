#input = "2\n9x34209asAb32sD840D9258 02934x2DoebAaab90CDEe348290\naabcwdefghkij ksdfopweiraa wieourslakaaier asjoirwekjaa"

file = open("test.txt", "r")
input = file.read()

# 0-9 A-Z a-z = 62
lines = input.split('\n');
totalLines = lines[0]
lines = lines[1:]

ans = ""
for line in lines:
	result = [0 for i in range(123)]
	phrases = line.split(' ');
	inc = 0
	for phrase in phrases:
		inc += 1
		for c in phrase:
			if result[int(ord(c))] == inc - 1:
				result[int(ord(c))] = inc

	for idx, r in enumerate(result):
		if r >= len(phrases):
			if(idx > 9):
				ans += chr(idx)
			else:
				ans += str(idx)
	print ans
	ans = ""

