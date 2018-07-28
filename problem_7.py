#My solution for problem 7 on Project Euler.

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

#Arbitrary large number.
primes = sieve(200000)
count = 0

#Check for when the 10,001st prime is reached. If the number given is too small, no result is printed.
for prime in primes:
    count += 1
    if count == 10001:
        print prime

