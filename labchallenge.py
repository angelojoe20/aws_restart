def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Finding prime numbers between 1 and 250
prime_numbers = []
for number in range(1, 251):
    if is_prime(number):
        prime_numbers.append(number)

# Define the file path where the results will be stored
file_path = "/home/ec2-user/results.txt"
with open(file_path, "w") as file:
    for prime in prime_numbers:
        file.write("{}\n".format(prime))

print("Prime numbers between 1 and 250 have been written to {}".format(file_path))
