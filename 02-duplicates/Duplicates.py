import collections
your_string=input()
b = your_string.lower()
d = collections.defaultdict(int)
for c in b:
    d[c] += 1
d = {k: v for k, v in d.items() if v>1}

print(d)
