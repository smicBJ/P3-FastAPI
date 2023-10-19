
total_run_count = 0


def my_decorator_function(func):

    def wrapper_function():
        global total_run_count

        func()

        total_run_count += 1
        print(total_run_count)

    return wrapper_function


def my_second_decorator_function(func):

    def wrapper_function():
        global total_run_count

        func()

        total_run_count += 2
        print(total_run_count)

    return wrapper_function


@my_decorator_function
@my_second_decorator_function
def email_student():
    print("Email Sent")


for _ in range(10):
    email_student()
