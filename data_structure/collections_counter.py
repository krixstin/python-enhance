from collections import Counter

c = Counter('sejin hajin woojin')
print(c)

# Counter({'j': 3, 'i': 3, 'n': 3, ' ': 2, 'o': 2, 's': 1, 'e': 1, 'h': 1, 'a': 1, 'w': 1})


text= "Set in 1997, the drama centers around a female high school student Shi Won, who idolizes boyband H.O.T. and her 5 high school friends in Busan. As the timeline moves back and forth between their past as 18-year-old high schoolers in 1997 and their present as 33-year-olds at their high school reunion dinner in 2012, one couple will announce that they're getting married."
sorted(Counter(text).items(), key = lambda t: t[1], reverse =True)