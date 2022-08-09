text = input()
letter = input()
lenLetter = len(letter)
lenText = len(text)
count = 0
if " " in text:
    nonSpaceText = text.replace(" ","")
for i in text:
    if i == letter:
        count += 1
freq = (count/lenText)*100
print(int(freq))
