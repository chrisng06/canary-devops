from collections import Counter
from sys import argv as s

def is_prime(n):
  if n == 1:
    return False
  if n % 2 == 0:
    return False
  i = 3
  while i * i <= n:
    if n % i == 0:
      return False
    i += 2
  return True

def prt_factors(pf_ct):
  pf_ct_dt = []
  for key in pf_ct.items():
    if key[1] == 1:
      b = str(key[0])
      pf_ct_dt.append(b)
    else:
      b = '**'.join(map(str, key))
      pf_ct_dt.append(b)
  print '*'.join(pf_ct_dt)


def prime_factors(n):
  prime_factor_list = []
  while not n % 2:
    prime_factor_list.append(2)
    n //= 2
  while not n % 3:
    prime_factor_list.append(3)
    n //=3
  i = 5
  while n!= 1:
    if is_prime(i):
      while not n % i:
        prime_factor_list.append(i)
        n //= i
    i += 2
  pf_ct = Counter(prime_factor_list)
  prt_factors(pf_ct)

n = int(s[1] if len(s)>1 else '')

pf_ct = prime_factors(n)
