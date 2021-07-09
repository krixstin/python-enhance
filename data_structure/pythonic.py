lang = "python, java, javascript, go"

#split()
lang_list = lang.split(",")
print(lang_list)

for each in lang.split(", "):
    print(each.strip()) #strip space added to in front of item

#assign
one, two, three, four = lang.split(", ")


#List comprehension
result = [i for i in range(11)]
print(result)

even = [i for i in range(1,11) if i%2==0]
print(even)

