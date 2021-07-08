dic={'Kristin':21,
    'Sophia':23}

for items in dic.items():
    print(items)
    print(type(items))

for k,v in dic.items():
    print(k,v)    

print("Gee" in dic.keys()) #false