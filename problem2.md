Problem 2. Get a computer program for distinguishing a randomly generated sequence of zeroes and ones from a cooked-up one. You are welcome to write the program yourself or use what can you find on the web or in some book. Test your program on the following two sequences: the sequence consisting of the concatenation of all numbers in binary form1
0 1 10 11 100 101 110 111 1000...
and a similar sequence consisting of the concatenation of all prime numbers in binary form
0 1 10 11 101 111 1011 ...
The first sequence (the fractional part of the Champernowne number) is known to be random when considered in base 10; the second sequence (the fractional part of the Copeland-Erd ̈os constant in binary form) is known to be random. In both cases, randomness is understood in a very specific way,2 and you are welcome to discuss this point too.


Implementation:
No python libraries used but built-in python functions utilized. 
Functions were created to implement logic and implementation for distinguising a randomly generated sequences of 0s and 1s from a cooked up one. 

Input validation: validates user input so the program can only accept a sequence of 0s, 1s, or spaces

Binary to decimal conversion:
Each binary number in the sequence is converted to its decimal equivalent (check readme for source)

Prime number check:
Checks whether each decimal value converted from binary is prime or not (check readme for source)

Sequence analysis:
If all decimal value conversions from binary are prime numbers, it will categorize the sequence as a concatenation of all prime numbers in binary form.
Else, it will categorize as a concatenation of all numbers in binary form.

IMPORTANT NOTE:
0 and 1 decimal values are not considered prime in this program (and in math generally).

Sequence 1:  0 1 10 11 100 101 110 111 1000
Output: The sequence is a concatenation of all numbers in binary form. 
Reasoning: 0 and 1 are not considered prime numbers when converted into decimal from binary. 

Sequence 2: 0 1 10 11 101 111 1011
Output: The sequence is a concatenation of all numbers in binary form. 
Reasoning: 0 and 1 are not considered prime numbers when converted into decimal from binary. 


Sequence 3: 10 11 100 101 110 111 1000
Output: The sequence is a concatenation of all numbers in binary form. 
Reasoning: Decimal values are 2 3 4 5 6 7 8. There are multiple non-prime values in the sequence after binary to decimal conversion. 

Sequence 4: 10 11 101 111 1011
Output: The sequence is a concatenation of all prime numbers in binary form.
Reasoning: Decimal values are 2 3 5 7 11. These are all prime values after binary to decimal conversion