
### sqaure root of x ###
def sqrt(x):
  i = 1.0
  j = 1.0
  mrgn = 0.000000000000001
  #adjusting for float representation
  mrgn *= (10**len(str(x)))
  while True:
    s=i*i
    if s < x:
      i+=j
    if s > x:
      i-=j
      j/=10
    if x == s or (x < s + mrgn and x > s - mrgn):
      return i

# print(sqrt(13))
# print(sqrt(9874))
# print(sqrt(66))
# print(sqrt(9859))
# print(sqrt(78532156))
# print(sqrt(84415))
# print(sqrt(136))
# print(sqrt(18))
# print(sqrt(984765))
# print(sqrt(13265))

def sqrt2(x):
  return x ** (1/2.0)

# print(sqrt2(13))
# print(sqrt2(9874))
# print(sqrt2(66))
# print(sqrt2(9859))
# print(sqrt2(78532156))
# print(sqrt2(84415))
# print(sqrt2(136))
# print(sqrt2(18))
# print(sqrt2(984765))
# print(sqrt2(13265))



### logarithm - base*ans = arg - returns ans ###
def log(base, arg):
  i = 1.0
  ans = 0
  mrgn = 0.000000000000001
  #adjusting for float representation
  mrgn *= 10**(int(len(str(base))) + int(len(str(arg)))-1)
  while True:
    if base ** ans < arg:
      ans += i
    if base ** ans > arg:
      ans -= i
      i /= 10.0
    if base ** ans == arg or (base ** ans < arg + mrgn and base ** ans > arg - mrgn) :
      return ans


# print(log(2, 300))
# print(log(61, 9519))
# print(log(61, 9519546))


### x factorial ###
def fctrl(x):
  i = 1 #skip 0!
  for j in range(1, x+1):
    i *= j
  return i

# print(fctrl(3))
# print(fctrl(4))
# print(fctrl(5))

### x factorial - recursive ###
def fctrl2(x):
  if x == 0:
    return 1
  return x * fctrl2(x-1)

print(fctrl2(3))
print(fctrl2(4))
print(fctrl2(5))

### eulers number ###
def euler(x):
  f=1
  e=1 #skips 0!
  for i in range(x):
    f *= (i+1)
    e += 1/f
  return e

#doesnt get more precise than 17 steps
# print(euler(17))

### eulers number ###
def euler2(x):
  ftl = lambda n : 1 if n == 0 else n * ftl(n-1)
  e=0
  return e + (1/ftl(x))
# not working properly
# print(euler2(17))


### find nth prime ###
def findPrime(n):
  if n <= 5:
    count = 0
    i = 1
    while count < n:
      i+=1
      for x in range(2, i):
        if i % x == 0:
          break
      else:
        count += 1
        if count == n:
          return i

  if n > 5:
    count = -1 #count 1 behind
    i = 1
    while count < n:
      i+=1
      for x in range(2, i//2):
        if i % x == 0:
          break
      else:
        count += 1
        if count == n:
          return i


# print(findPrime(1))
# print(findPrime(2))
# print(findPrime(3))
# print(findPrime(4))
# print(findPrime(5))
# print(findPrime(6))
# print(findPrime(7))
# print(findPrime(8))
# print(findPrime(9))
# print(findPrime(10))

# print(findPrime(11))
# print(findPrime(100))
# print(findPrime(1000))
# print(findPrime(2000))
# print(findPrime(3000))
# print(findPrime(3001))


### returns pairs of factors ###
def findfactors(x):
  fctrs = []
  pairs = {}
  for i in range(1, x+1):
    if x % i == 0:
      fctrs.append(i)
      if  i*i == x: #perfect squares appened twice
        fctrs.append(i)

  for i in range(len(fctrs)//2):
    pairs[fctrs[i]] = fctrs[(-i)-1]

  return pairs

print(findfactors(4))
print(findfactors(19))
print(findfactors(435))
print(findfactors(9846))
print(findfactors(684))
print(findfactors(56499))
print(findfactors(1084765))