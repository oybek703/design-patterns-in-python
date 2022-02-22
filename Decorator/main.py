import time


def time_it(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f'{func.__name__} took execution time: {int(end - start) * 1000}ms')

    return wrapper

@time_it
def some_operation():
    print('Starting some operation...')
    time.sleep(2)
    print('We are done!')
    return 123


some_operation()
