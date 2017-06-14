from python import test


def get_answer(final_number=1000):
    sum = 0
    for i in range(1, final_number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    return sum


test.running_time(get_answer)