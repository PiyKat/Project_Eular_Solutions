'''

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

'''

# def check_if_prime(n):
#
#     prime_factors = [i for i in range(1,n+1) if n%i == 0]
#
#     if prime_factors == [1,n]:
#         return True
#     else:
#         return False

def check_if_prime(n,prime_factors):

    #prime_factors = [i for i in range(1,n+1) if n%i == 0]

    if n == 2:
        #prime_factors.append(n)
        return True
    elif n % 2 == 0:
        return False
    else:
        prime_check = [n % i for i in prime_factors]

        for remainders in prime_check:

            if remainders != 0:

                if prime_check.index(remainders) == len(prime_check) - 1:
                    prime_factors.append(n)
                    return True
                else:
                    continue

            else:
                return False



def prime_sum(number_limit):

    ## We assign sum two for the sake of reducing the search space by nearly half

    sum = 2
    prime_factors = [2]

    for i in range(3,number_limit+1):

        if i % 2 != 0 :

            if check_if_prime(i,prime_factors):

                sum += i
                print(sum)

    return sum

print(prime_sum(3000000))
