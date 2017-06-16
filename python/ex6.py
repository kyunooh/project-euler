import test


def get_answer(end_num=100):
    return answer(end_num)


def answer(end_num):
    sum_of_the_square = 0
    sums = 0
    for i in range(end_num + 1):
        sums += i
        sum_of_the_square += i ** 2
    square_of_the_sum = sums ** 2

    return square_of_the_sum - sum_of_the_square

print(get_answer())
assert(get_answer(10) == 2640)

test.running_time(get_answer)