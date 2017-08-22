'''

The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''

def return_difference(limit = 100,exp = 2):

    sum_squared = 0
    squared_sum = 0

    for number in range(1,limit+1):

        sum_squared += number
        squared_sum += number ** exp

    return sum_squared**exp - squared_sum

print(return_difference())


