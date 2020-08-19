import math
text = "X-DSPAM-Confidence:    0.8475";
i=0;
for letter in text:
    try:
        letter=float(letter)
    except:
        i=i+1
        continue
num=float(text[i:])
print(num)
