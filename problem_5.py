'''

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

'''

### Note, the function can be used to find the no that is divisible by any range no in python

def find_lcm(start,end):

    lcm = 1

    range_list = [i for i in range(start,end)]

    while(range_list != [1]*len(range_list)):

        if 1 in range_list:
            range_list.remove(1)

        divisor = min(range_list)

        for numbers in range_list:

            if numbers % divisor == 0:
                range_list[range_list.index(numbers)] /= divisor

        lcm *= divisor

    return lcm

print(find_lcm(10,20))