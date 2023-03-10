def calculateCompoundInterest():
    
# This first 3 lines are provided for yougetACompoundInterest()
# This first 3 lines are provided for you
 def compound_interest(principal, time, rate):
    A = principal * ((1 + rate/100) ** time)
    Interest = A - principal

    print('Compound Interest:', round(Interest, 2))

 line_break = "---"
 principal = float(input("Principle (amount): "))
 time =      float(input("Time:               "))
 rate =      float(input("Rate:               "))

 compound_interest(principal, time, rate)
 print(line_break)

 principal = float(input("Principle (amount): "))
 time =      float(input("Time:               "))
 rate =      float(input("Rate:               "))

 compound_interest(principal, time, rate)
 print(line_break)

 principal = float(input("Principle (amount): "))
 time =      float(input("Time:               "))
 rate =      float(input("Rate:               "))

 compound_interest(principal, time, rate)
 
    # end assignment

## If you want to test locally run > python compoundInterest.py

if __name__ == "__main__":
    calculateCompoundInterest()
