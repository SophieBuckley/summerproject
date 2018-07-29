#My solution for problem 10 on Project Euler.

#General function to perform the sieve of Eratosthenes algorithm.
def sieve(n):

  a = []

  for i in range(2, n):
    a.append(True)
  
  for i in range(2, int(n**0.5)):
    if a[i-2] == True:
      j = i**2
      while j < n:
        a[j-2] = False
        j += i

  primes = []
  m = 2

  for e in a:
    if e:
      primes.append(m)
    m += 1
    
  return primes

#Call sieve with n = 2000000.
primes = sieve(2000000)
total = 0

#For each prime number, add it to total, up to n.
for prime in primes:
    total += prime

print total
