import test


def get_answer():
    return get_smallest_multiple()


def is_not_smallest_multiple(number):
    for i in range(2, 20):
        if number % i != 0:
            return True
    return False


def get_smallest_multiple(end_num=20):
    primes = []
    prime_candidate = range(2, end_num)
    for i in prime_candidate:
        is_prime = True
        for j in range(2, i - 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    max_exp_num_list = []
    for i in primes:
        p = i
        while True:
            exp_num = p * i
            if exp_num > end_num:
                max_exp_num_list.append(p)
                break
            p = exp_num

    answer = 1
    for i in max_exp_num_list:
        answer *= i
    return answer


print(get_answer())

test.running_time(get_answer)
