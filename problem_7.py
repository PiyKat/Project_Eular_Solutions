'''

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

#### The code written below will print out nth prime number, where n is defined by the user

import sys


def check_if_prime(n):

    prime_factors = [i for i in range(1,n+1) if n%i == 0]

    if prime_factors == [1,n]:
        return True
    else:
        return False


def prime_no(no):

    counter = 1
    #prime_no = 0
    while(counter != no):

        for i in range(2,sys.maxsize):
            # We can further reduce the search space by half, as any even number will never be a prime

            if i % 2 != 0:

                if check_if_prime(i):
                    counter += 1

                    if counter == no :
                        return i

print(prime_no(10001))