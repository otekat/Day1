from math import sqrt


def generatePrimeNumbers(num):
    prime_list = []
    numbers_types = (int, float, complex)
    if isinstance(num, numbers_types):
        if num >= 3:
            prime_list.append(2)
            nextprime = 3
            while nextprime < num:
                isprime = True
                sqrt_value = sqrt(nextprime)
                sample_range = [i for i in prime_list if i <= sqrt_value]
                for i in sample_range:
                    if nextprime % i == 0:
                        isprime = False
                        break
                if isprime:
                    prime_list.append(nextprime)
                nextprime += 2
            return prime_list
        else:
            raise ValueError
    else:
        raise TypeError


print(generatePrimeNumbers(50))

