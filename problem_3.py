#My solution for problem 3 on Project Euler.

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

m = 600851475143
primes  = sieve(int((m)**0.5))
prime_factors = []

for i in primes:
  if m % i == 0:
    prime_factors.append(i)
  i += 1

print prime_factors[-1]
