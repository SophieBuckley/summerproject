#My solution for problem 1 on Project Euler.

def solution(end):
	print sum(n for n in range(end) if n % 3 == 0 or n % 5 == 0)

solution(1000)
