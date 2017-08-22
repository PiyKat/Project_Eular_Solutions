'''

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

'''


### Note - This code will give you the correct answer to any no of digits you may want by changing the "no of digits" parameter


##### METHOD 1 - Brute Force ########


def check_palindrome(n):

    original_number = n

    quotient = 1

    palindrome = 0

    while (n != 0):

        last = n % 10
        palindrome = 10 * palindrome + n % 10
        #numbers.append(last)
        n = int(n / 10)

    #palindrome = 0
    #indexes = 10 ** (len(numbers) - 1)

    return palindrome == original_number



def greedy_method(no_of_digits):

    palindrome = []

    for first in range(10**(no_of_digits - 1),10**(no_of_digits) - 1):

        for second in range(10**(no_of_digits - 1),10**(no_of_digits) - 1):

            check_no = first * second

            if check_palindrome(check_no):
                palindrome.append(check_no)

    return max(palindrome)


print(greedy_method(3))