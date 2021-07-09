# python-enhance

## 1. count_strings.py 
After receiving word from user, it check how many time the word repeats in Martin Luther King's "I have a dream" speech 

( use ***source\I have a dream speech.txt*** )


## 2. command_analyzer.py
It generates a dictionary of user ID with the most frequent command on server in a desending order
* ***import csv***

( use ***source\command_data.csv*** )


## 3. count_words.py
For the text entered by user, it returns the dictionary of words that repeated the most to least with frequency

* ***defaultdict()***

* ***sorted(d.items(), key=lambda kv: kv[1], reverse= True)***
