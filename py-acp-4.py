num = int(input("Enter a number: "))
num_str = str(num)
num_len = len(num_str)

sum_of_powers = 0

for digit in num_str:
    sum_of_powers += int(digit) ** num_len

if sum_of_powers == num:
    print(num, "is an Armstrong number!")
else:
    print(num, "is not an Armstrong number.")