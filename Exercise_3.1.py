#The solution for the problem 3.1:

hrs = input("Enter Hours:")
h = float(hrs)
rate = float(input("Enter the Rate:"))
if h > 40:
    pay = (h - 40) * rate * 1.5 + 40 * rate
print(pay)
