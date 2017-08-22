'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''




### The code first reduces the search space by half by checking if the number is divisible by 2
#### Then we use the fundamental theorem of arithmetic to check if the number is actalluy prime number or not



def check_if_prime(n,prime_factors):

    #prime_factors = [i for i in range(1,n+1) if n%i == 0]

    if n == 2:
        prime_factors.append(n)
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
                #return True


    # if prime_factors == [1,n]:
    #     return True
    # else:
    #     return False


def prime_numbers(number):

    prime_factors = []
    number_prime_factors = []

    for i in range(2,number):
        #print(i)
        check  = check_if_prime(i,prime_factors)

        if check == True:

                 if number % i == 0:
                     print("FOUND ONE  :  " ,str(i))
                     print(prime_factors)
                     number_prime_factors.append(i)

            #print(prime_factors)
    return max(number_prime_factors)


print(prime_numbers(13195))