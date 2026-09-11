# Exercise 1
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
# Exercise 2
def count_digits(n):
    if n<10:
        return 1
    return count_digits(n//10)+1
    pass

# Exercise 3
def sum_digits(n):
    if n < 10:
        return n
    return sum_digits(n // 10) + n%10
    pass
