#CARD-VALIDATOR

sum_odd_digits = 0
sum_even_digits = 0
total=0
CARD_NUMBER = (input("ENTER YOUR CARD NUMBER: "))
CARD_NUMBER = CARD_NUMBER.replace("-","")
CARD_NUMBER = CARD_NUMBER.replace("-","")
CARD_NUMBER = CARD_NUMBER[::-1]

for x in CARD_NUMBER[::2]:
    sum_odd_digits += int(x)
for x in CARD_NUMBER[1::2]:
    x = int(x)*2
    if x>=10:
        sum_even_digits += (1+(x%10))
    else:
        sum_even_digits += int(x)


total = sum_even_digits + sum_odd_digits

if total%10 == 0:
    print("VALID")
 
else:
    print("INVALID")