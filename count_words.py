from collections import defaultdict

# raw_text = input("Enter your text")
raw_text = "This is is is your your your your your text"
d = defaultdict(lambda: 0)
text = raw_text.lower().split()

for word in text:
    d[word]+=1
    
most_to_least=sorted(d.items(), key=lambda kv: kv[1], reverse= True)
print(most_to_least)
