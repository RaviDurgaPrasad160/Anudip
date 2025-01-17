# 3. Python program to check if a given number is an Armstrong number 

number = int(input("Enter a number: "))
digits = [int(d) for d in str(number)]
sum_of_powers = 0
for d in digits:
    sum_of_powers += d ** len(digits)

if sum_of_powers == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
