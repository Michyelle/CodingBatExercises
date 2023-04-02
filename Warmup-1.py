"""
> sleep_in
The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation.
We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.

sleep_in(False, False) → True
sleep_in(True, False) → False
sleep_in(False, True) → True
"""
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

"""
> diff21
Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.

diff21(19) → 2
diff21(10) → 11
diff21(21) → 0
"""
def diff21(n):
  if (n > 21):
    diff = 21 - n
    abs(diff)
    diff += diff
  else:
    diff = 21 - n
  return abs(diff)

"""
> near_hundred
Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.

near_hundred(93) → True
near_hundred(90) → True
near_hundred(89) → False
"""
def near_hundred(n):
  if (n >= 90 and n <= 110) or (n >= 190 and n<= 210):
    return True
  else:
    return False
  
"""
> not_string
Given a string, return a new string where "not " has been added to the front. However, if the string already begins
with "not", return the string unchanged.

not_string('candy') → 'not candy'
not_string('x') → 'not x'
not_string('not bad') → 'not bad'
"""
def not_string(str):
  addnot = "not"
  if addnot in str[0:3]:
    return str
  else:
    newstr = addnot + " " + str[0:]
    return newstr
  
"""
> missing_char
Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of
n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).

missing_char('kitten', 1) → 'ktten'
missing_char('kitten', 0) → 'itten'
missing_char('kitten', 4) → 'kittn'
"""
def missing_char(str, n):
  return str[:n] + str[n+1:]  
  
  
  
  
  
  
  
  
  
  
  
  
"""
> sum_double
Given two int values, return their sum. Unless the two values are the same, then return double their sum.

sum_double(1, 2) → 3
sum_double(3, 2) → 5
sum_double(2, 2) → 8
"""
def sum_double(a, b):
  if (a != b):
    return a + b
  else:
    return 2 * (a+b)

"""
> makes10
Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.

makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
"""
def makes10(a, b):
  if (a == 10) or (b == 10) or (a + b == 10):
    return True
  else:
    return False

"""
> front3
Given a string, we'll say that the front is the first 3 chars of the string. If the string length is less than 3,
the front is whatever is there. Return a new string which is 3 copies of the front.

front3('Java') → 'JavJavJav'
front3('Chocolate') → 'ChoChoCho'
front3('abc') → 'abcabcabc'
"""
def front3(str):
  newstr = str[0:3]
  newstr = newstr * 3
  return newstr
