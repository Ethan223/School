#!usr/bin/python3/
#***************************************************
#Name: Ethan Coles
#ID: 0843081
#File: sieve.py
#Description: CIS*3190 Assignment 4, Python implementation
#of Sieve of Eratosthenes algorithm.
#***************************************************
import sys

#Ask for upper limit and check if valid
try:
    upperLimit = int(input("Enter an upper limit: "))

    if upperLimit < 2 or upperLimit > 999999999:
        print("Error: Invalid limit value")
        sys.exit()
except ValueError:
    print("Error: Input not an integer")
    sys.exit()

#Initialize array of numbers
primeSet = []
for i in range(2,upperLimit+1):
    primeSet.append(i)

#Main algorithm
for i in range(0,upperLimit-1):
    if primeSet[i] != 0:
        for j in range(i+1,upperLimit-1):
            if primeSet[j]%primeSet[i] == 0:
                primeSet[j] = 0

#Output to file
fp = open("output.txt", "w")

for i in range(0,upperLimit-1):
    if primeSet[i] != 0:
        fp.write(str(primeSet[i]) + "\n")

fp.close()
print("Successfully wrote prime numbers to output.txt.")
            