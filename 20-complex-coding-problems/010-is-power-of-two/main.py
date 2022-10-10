
from timeit import timeit


def is_power_of_two_usual(num):
    # Usual method to check
    if (num < 0):
        return False
    elif (num == 1):
        return True
    n = 2
    while(num > n):
        n = n*2
    return n == num


def is_power_of_two_clever(num):
    # Clever method to check
    return num > 0 and (num & (num-1)) == 0


if __name__ == '__main__':
    num = pow(2, 21)
    time_usual = timeit(lambda: is_power_of_two_usual(num), number=10000)
    time_clever = timeit(lambda: is_power_of_two_clever(num), number=10000)
    print(f"Time for usual method  : {time_usual:0.5f}")
    print(f"Time for clever method : {time_clever:0.5f}")
