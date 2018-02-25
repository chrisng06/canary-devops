from collections import Counter
from sys import argv as s
import primefac

n = int(s[1] if len(s)>1 else '')

factors = list(primefac.primefac(n) )
pfactor_ct = Counter(factors)

pfactors = []
for key in pfactor_ct.items():
  if key[1] == 1:
    b = str(key[0])
    pfactors.append(b)
  else:
    b = '**'.join(map(str, key))
    pfactors.append(b)
print '*'.join(pfactors)
