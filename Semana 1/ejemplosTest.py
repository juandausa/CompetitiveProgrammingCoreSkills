import time

def main():
  inicio = time.time()
  print(solve1(getTest()))
  fin = time.time() - inicio
  print(fin)

def solve1(a):
  max = 0
  for x in a:
    if x > max:
      max = x
  return max
  
def solve2(a):
  max = 0
  for i in range(len(a)):
    for j in range(len(a)):
      if i != j and a[i] + a[j] > max:
        max = a[i] + a[j]
  return max

def solve3(n):
  ans = 0
  for i in range(n):
    for j in range(n):
      if i < j and (i + j) % 2 == 0:
        ans += 1
  return ans

def solve4(s):
  toDelete = s[0]
  others = ""
  for c in s:
    if c != toDelete:
      others += c
  s = others
  
  #prefix of length 1 surely doesn't contain different letters
  prefix = s[0]
  for i in range(1, len(s)):
    #each letter should be the same as the first
    if s[i] == prefix[0]:
      prefix += s[i]
    else:
      break
  return prefix

def getTest():
  return [-1,-2,-3]

main()