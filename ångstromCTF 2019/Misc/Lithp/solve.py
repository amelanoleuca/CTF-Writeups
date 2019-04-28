import math

encrypted = [8930, 15006, 8930, 10302, 11772, 13806, 13340, 11556, 12432, 13340, 10712, 10100, 11556, 12432, 9312, 10712, 10100, 10100, 8930, 10920, 8930, 5256, 9312, 9702, 8930, 10712, 15500, 9312]
reorder = [19, 4, 14, 3, 10, 17, 24, 22, 8, 2, 5, 11, 7, 26, 0, 25, 18, 6, 21, 23, 9, 13, 16, 1, 12, 15, 27, 20]

def enc(plain):
	uwuth = multh(plain)			# n => n(n-1)
	uwuth = owo(uwuth)				# reorder
	return uwuth

# n(n-1) for n in plain
def multh(plain):
	if plain == "":
		return []
	return [whats(plain[0]-1, plain[0])] + multh(plain[1:])

# undoes multh with quadratic formula
def unmulth(flavored):
	return [int(math.sqrt(4*n+1)-1)//2 for n in flavored]

# shuffles items by reorder
def owo(input):
	out = []
	for n in reorder:
		out.append(input[n])
	return out

# unshuffles
def uwu(input):
	out = [0]*len(input)
	for k in range(len(reorder)):
		out[reorder[k]] = input[k]
	return out

# multiplication
def whats(x, y):
	if y == 0:
		return 0
	return whats(x, y-1) + x


# print(encrypted)
unshuffle = uwu(encrypted)
# print(unshuffle)
reduced = unmulth(unshuffle)
# print(reduced)
print("".join(chr(c+1) for c in reduced))