'''

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

'''




### The code first reduces the search space by half by checking if the number is divisible by 2
#### Then we use the fundamental theorem of arithmetic to check if the number is actalluy prime number or not

def if_prime(n):

    prime_factors = [i for i in range(1,n+1) if n%i == 0]
    #print(prime_factors)

    if prime_factors == [1,n]:
        #print(prime_factors)
        return True
    else:
        return False


# def if_prime(i,prime_factors):
#
#     #prime_factors = [i for i in range(1,n+1) if n%i == 0]
#
#     if i == 2:
#
#         return True
#
#     else:
#
#         prime_check = [i % j for j in prime_factors]
#
#         for remainders in prime_check:
#
#             if remainders != 0:
#
#                 if prime_check.index(remainders) == len(prime_check) - 1:
#
#                     return True
#                 else:
#                     continue
#
#             else:
#                 return False
                #return True



def generate_multiples(factor,n,number_list):

    #multiple_list = []
    multiple = factor
    i = 1

    while(multiple*i < n):


        #multiple_list.append(multiple)
        #print(multiple *i)
        try:
            number_list.remove(multiple*i)
        except ValueError as e:
            pass
            #print(str(multiple*i) + " has already been deleted")

        i += 1

    return number_list


def prime_numbers(n):

    prime_factors = []

    try:
        number_list = [i for i in range(2,n+1)]

    except:
        print("The array cannot be initialized")

    #while(len(number_list) != 0):
    #print("WHILE LOOP !!!")

    for i in number_list:
            #print(i)

            if if_prime(i):

                prime_factors.append(i)
                print(prime_factors[-1])
                number_list = generate_multiples(i,n,number_list)


    return prime_factors


print(max(prime_numbers(13195)))