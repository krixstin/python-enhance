s= set([1,1,1,1,1,2,3,4,5,8])
print(s) # [1,2,3,4,5,8] only unique values

s.add(2)
s.remove(4)
s.discard(1)
# s.clear()

s2=set([10,20,30])

print(s.union(s2))
print(s & s2)
print(s | s2)

