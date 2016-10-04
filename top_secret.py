
file = open("Top-secret_InputForSubmission_1.txt", "r")
input = file.read()

lines = input.split('\n');

cipherCounter = 0

for line in lines:
	ans = ""
	cipher = line.split("|")[1]
	plaintext = line.split("|")[0]
	for c in plaintext:
		if(ord(c) >= 65 and ord(c) <= 91):
			result = ( (ord(c)-65) + (ord(cipher[cipherCounter])-65) ) % 26
			cipherCounter += 1
			if (cipherCounter == len(cipher)):
				cipherCounter = 0
			ans += (chr(result+65))
		elif(ord(c) > 96 and ord(c) <= 122):
			result = ( (ord(c)-97) + (ord(cipher[cipherCounter])-65) ) % 26
			cipherCounter += 1
			if (cipherCounter == len(cipher)):
				cipherCounter = 0
			ans += chr(result+97)
		else:
			ans += c
		print ans
		ans = ""
