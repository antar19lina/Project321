# PYTHON COMPOUND  INTEREST CALCULATOR
''' FORMULA FOR CALCULATING INTEREST :- 
A = P(1+r/n)^t
P = initial principal  balance
r = interest rate
t = no. of time period elapsed
A = final amount
'''
principle = 0
rate=0
time=0
#PRINCIPLE 
while True:
    principle=float(input("Enter a principle amount: "))
    if principle < 0:
        print("Principle cant be less than  zero")
    else:
         break
#RATE
while True:
    rate=float(input("Enter a rate of interest: "))
    if rate < 0:
        print("rate of interest cant be less than zero")
    else:
        break
#TIME
while True:
    time=int(input("Enter time: "))
    if time < 0:
        print("time cant be less than zero")
    else: 
        break
print(principle)
print(rate)
print(time)

TOTAL_AMOUNT = principle*pow(1+rate/100,time)
print(f"Balance after {time} year/s: {TOTAL_AMOUNT:+,.2f}Rs")
