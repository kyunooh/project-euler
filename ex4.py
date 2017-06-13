import time


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


def get_answer(palindrome_number):
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


assert(is_palindrome_number(1))
assert(not is_palindrome_number(13))
assert(is_palindrome_number(11))
assert(is_palindrome_number(9009))
assert(not is_palindrome_number(9909))

startTime = time.time()
for i in range(0, 100):
    print(get_answer(0))
endTime = time.time()
print(endTime - startTime)


def get_max_palindromes():
    found = False
    palindromes = []
    for i in range(1000, 100, -1):
        for j in range(1000, 100, -1):
            if is_palindrome_number(i * j): found = True; break
        if found: palindromes.append(i*j)
    print(max(palindromes))

startTime = time.time()
for i in range(0, 100):
    get_max_palindromes()
endTime = time.time()
print(endTime - startTime)
