#My solution for problem 6 on Project Euler.

sum_nat = 0
sum_squ = 0

for i in range (1, 101):
	sum_nat += i
	sum_squ += i**2

diff = sum_nat**2 - sum_squ

print diff
	
