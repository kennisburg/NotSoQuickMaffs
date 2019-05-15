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

# print(sqrt(8))
# print(sqrt(11))
# print(sqrt(12))
# print(sqrt(77))
# print(sqrt(777))
# print(sqrt(7777))
# print(sqrt(565))
# print(sqrt(984))
# print(sqrt(3216))
# print(sqrt(79846))
# print(sqrt(984351))

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


print(log(2, 300))
print(log(61, 9519))
print(log(61, 9519546))



def fctrl(x):
  i = 1 #skip !0
  for j in range(1, x+1):
    i *= j
  return i

# print(factorial(3))



def euler(x):
  f=1
  e=1 #skip !0
  for i in range(x):
    f *= (i+1)
    e += 1/f
  return e

#doesnt get more precise than 17 steps
# print(euler(17))

