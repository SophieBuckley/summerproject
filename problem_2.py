#My solution for problem 2 on Project Euler.

def solution():
  
  x = 1
  y = 1
  z = 0
  total = 0

  while z <= 4000000:
    z = x + y
    if z % 2 == 0:
      total += z
    x = y
    y = z

  print total
    
solution()
