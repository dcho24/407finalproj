
def binarytodecimal(binary):
    #converts binary string to decimal number
    return int(binary, 2)

def prime(n):
    #checks if the decimal value is prime or not
    if n < 2:
        return False

    for i in range(2,int(n/2) + 1):
        if (n % i) == 0:
            return False
    return True

def isbinaryprime(binary):
    #checks if decimal conversion of a binary string is prime
    decimal = binarytodecimal(binary)
    return prime(decimal)

def checksequence(sequence):
    #given user input of binary sequence, checks if sequence is prime or not
    #prime = Copeland Erdos case, all numbers including non-prime = Champernowne case
    binary_numbers = sequence.split()
    all_prime = True

    for binary in binary_numbers:
        if not isbinaryprime(binary):
            all_prime = False
            break

    if all_prime:
        return "The sequence is a concatenation of all prime numbers in binary form"
    else:
        return "The sequence is a concatenation of all numbers in binary form"

    
#user input of sequence checks
user_sequence = input("Enter a sequence of 0s and 1s separated by spaces: ")

#validation of input for only 0s and 1s and spaces
validinput = True
if all(char in '01 ' for char in user_sequence):
    result = checksequence(user_sequence)
    print(result)
else:
    print("Invalid input. Please enter a sequence of only 0s and 1s separated by spaces.")

