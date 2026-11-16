P = Initial_Balance = int(float(input("Enter the amount you would like to invest: ")))
t = Time_Period = int(float(input("Enter how long you would love to keep your money (in years): ")))
r = Interest_Rate = int(float(input("Enter your interest rate (%): ")))

total = P * pow(1 + r/100 , t)
print(f"Total balance is {total:.2f}")