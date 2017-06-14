import time

import test


def get_max_palindrome_number(palindrome_number):
    if not palindrome_number:
        max_three_digit_number = 999 * 999
        palindrome_number = max_three_digit_number
    else:
        palindrome_number -= 1

    while not (is_palindrome_number(palindrome_number)):
        palindrome_number -= 1

    return palindrome_number


def is_palindrome_number(n):
    int_list = str(n)
    return int_list == int_list[::-1]


def get_answer(palindrome_number=None):
    if not palindrome_number:
        palindrome_number = get_max_palindrome_number(0)

    divisor = 999
    while palindrome_number / divisor < 999:
        while palindrome_number % divisor != 0:
            divisor -= 1
            if palindrome_number / divisor > 999:
                palindrome_number = get_max_palindrome_number(palindrome_number)
                divisor = 999
                break
        if palindrome_number % divisor == 0:
            break

    return palindrome_number


test.running_time(get_answer)
