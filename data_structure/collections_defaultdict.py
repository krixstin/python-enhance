# KeyError: 'first'
d =dict()
# print(d["first"])

from collections import defaultdict

def default_value():
    return 100;

d= defaultdict(default_value)

print(d["first"])
print(d["not existing key"])