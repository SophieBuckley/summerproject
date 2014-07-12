#My solution for problem 6 on Project Euler.

sum_nat = 0
sum_squ = 0

for n in range (1, 101):
	sum_nat += n
	sum_squ += n**2

diff = sum_nat**2 - sum_squ

print diff
	
