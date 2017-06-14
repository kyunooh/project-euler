import test

def get_answer(number=600851475143):
    return get_prime_factors(number)


def get_prime_factors(number):
    available_numbers = []
    if number % 2 == 0:
        available_numbers.append(2)

    i = 3
    while i < number:
        if number % i == 0:
            available_numbers.append(i)
        if len(available_numbers) > 0 and number / available_numbers[-1] < i:
            break
        i += 2

    prime_numbers = available_numbers
    for i in available_numbers:
        prime_numbers = list(filter(lambda x: x % i != 0, prime_numbers))
        if len(prime_numbers) == 1:
            break

    return prime_numbers[0]


test.running_time(get_answer)