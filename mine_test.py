from hashlib import sha256


def num_zeros(s, n):
	return s[0:n] == "0" * n

data = "Test data"
n = 0
check = data + str(n)
check_hash = sha256(check.encode()).hexdigest()

while not num_zeros(check_hash, 6):
	# print(f"Str: {check} hash: {check_hash}")
	n += 1
	check = data + str(n)
	check_hash = sha256(check.encode()).hexdigest()

print(n)
