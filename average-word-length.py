text = input()
splitten = text.split()
count = 0
for i in splitten:
    count += 1
for a in text:
    replacedText = text.replace(" ","")
avg = len(replacedText)/count
print(avg)
