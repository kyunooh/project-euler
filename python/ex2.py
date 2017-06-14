import test

def get_answer():
    fibonacci_list = get_fibonacci_list()
    fibonacci_list_sum = sum(filter(lambda x: x % 2 == 0, fibonacci_list))
    return fibonacci_list_sum


def get_fibonacci_list(under=4000000):
    fibonacci_list = [1, 2]
    while True:
        fibonacci = next_fibonacci(fibonacci_list[-2], fibonacci_list[-1])
        if fibonacci > under:
            break
        fibonacci_list.append(fibonacci)

    return fibonacci_list


def next_fibonacci(first, second):
    return first + second

test.running_time(get_answer)