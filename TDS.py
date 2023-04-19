# Get the three input numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Compare the numbers using if-elif statements
if num1 >= num2 and num1 >= num3:
    largest_num = num1
elif num2 >= num1 and num2 >= num3:
    largest_num = num2
else:
    largest_num = num3

# Print the largest number
print("The largest number is:", largest_num)
