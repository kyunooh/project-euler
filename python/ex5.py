import test


def get_answer():
    return get_smallest_multiple()


def is_not_smallest_multiple(number):
    for i in range(2, 20):
        if number % i != 0:
            return True
    return False


def get_smallest_multiple():
    solution_number = 2
    while is_not_smallest_multiple(solution_number):
        solution_number += 1
    return solution_number


test.running_time(get_answer)
