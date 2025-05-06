num = int(input("Enter a number: "))

num_str = str(num)
num_len = len(num_str)

sum_of_powers = 0
for digit in num_str:
    digit = int(digit)
    power = 1
    count = 0
    while count < num_len:
        power = power * digit
        count = count + 1
    sum_of_powers = sum_of_powers + power

if sum_of_powers == num:
    print("This is an Armstrong number")
else:
    print("This is not an Armstrong number")
