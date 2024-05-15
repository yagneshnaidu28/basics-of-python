# Step 1: Get the number from the user
num = int(input("Enter a number: "))

# Step 2: Calculate the number of digits
num_digits = len(str(num))

# Step 3: Calculate the sum of digits raised to the power of the number of digits
temp_num = num
sum_of_digits = 0

while temp_num > 0:
    digit = temp_num % 10
    sum_of_digits += digit ** num_digits
    temp_num //= 10

# Step 4: Check if the number is an Armstrong number
if num == sum_of_digits:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
