import math


def find_next_prime(p):
	'''Given prime p, return the next largest prime'''
	# Edge cases
	if p == 2:
		return 3
	if p % 2 == 0:
		return None

	# Test only up to the square root of the new prime
	lim = int(math.ceil(math.sqrt(p + 2)))

	found_flag = False

	# Test every odd
	p_next = p + 2

	while not found_flag:
		if all((p_next % i != 0) for i in xrange(2, lim + 1)):
			found_flag = True
			break
		p_next += 2

	return p_next


def nth_prime(n):
	'''Display the nth prime number'''
	primes = [2, 3]
	if n < 1:
		return 2
	elif n == 2:
		return 3

	while len(primes) < n:
		p = primes[-1]
		p_next = find_next_prime(p)
		primes.append(p_next)

	return primes[-1]
