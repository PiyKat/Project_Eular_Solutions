'''

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

'''

def get_pythog_trip(add_limit):

    for i in range(add_limit):
        for j in range(i+1,add_limit):
            for k in range(j+1,add_limit):

                if i**2 + j**2 == k**2:
                    if i + j + k == 1000:
                        return i*j*k

print(get_pythog_trip(1000))