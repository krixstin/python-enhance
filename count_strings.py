from io import open_code


file = open("source\I have a dream speech.txt")

text = ""
while True:
    line= file.readline()
    if not line:
        break
    text = text + line.strip() + "\n"

file.close()
word = input("Type a word to count in your file")
word_count = text.upper().count(word.upper())
print('"'+word.upper() +' "' + " appears " + str(word_count) +" times in your file")