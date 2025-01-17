# 1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division. 

def div(num1, num2):
    if num2 != 0:
        return round(num1 / num2, 2)
    return 'Can not divide by zero'

result = div(35,5)

print(result)