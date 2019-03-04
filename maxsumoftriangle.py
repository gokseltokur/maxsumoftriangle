""" Goksel Tokur """

import math
import sys


def maxpath(matrix):
    #Change primes with minimum integer value
    executePrimes(matrix)

    # i = row, j = column
    for i in range(len(matrix)-2, -1, -1):
        for j in range(i+1):
            # If current value is prime do not execute code.
            if isPrime(matrix[i][j]):
                continue


            # Middle adjacent is more than rigt.
            if matrix[i+1][j] > matrix[i+1][j+1]:
                matrix[i][j] += matrix[i+1][j]
            # Right adjacent is more than middle.
            elif matrix[i+1][j] < matrix[i+1][j+1]:
                matrix[i][j] += matrix[i+1][j+1]
            # Right and middle is equal each other.
            elif matrix[i+1][j] == matrix[i+1][j+1]:
                matrix[i][j] += matrix[i+1][j]
            #print(matrix)
    return matrix[0][0]

#To check prime or not.
def isPrime(n):
    if n > 1:
        for i in range(2,n):
            if n % i is 0:
                return False
        else:
            return True
    else:
        return False

#Change primes with minimum integer value
def executePrimes(matrix):
    for i in range(len(matrix)):
        for j in range(i+1):
            if isPrime(matrix[i][j]):
                matrix[i][j] = -sys.maxint - 1

# This method to get input from txt file. (input.txt)
def moveTxttoMatrix():
    matrix = [[int(i) for i in line.split()] for line in open('input.txt')]

    return matrix


m = moveTxttoMatrix()
print(maxpath(m))
