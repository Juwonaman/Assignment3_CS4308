import time
# time to calculate the time when it starts and when it ends
def float_multi(n):
    times = 1.0
    for _ in range(n):
        times *= 1.0001
    return times
# a function that takes in one argument, and then it loops through how many times that argument has and multiples and adds
# the times that is initialized with 1.0001, when it is done it returns the result
def int_multi(n):
    times = 1
    for _ in range(n):
        times *= 1
    return times
# this is also a function that takes in an argument, but it is in an int now. it loops through how many n and adds and multiples it by 1, then it returns the result
try:
    user_input = input("Enter the number of operations to perform, separated by commas (e.g., 10000000,50000000,100000000): ")
    test_cases = [int(x.strip()) for x in user_input.split(",")]
except ValueError:
    print("Invalid input. Please enter valid integers separated by commas.")
    exit(1)
# this try block prompts the user to enter in numbers in a certain format with "," seperating the numbers.
# it then splits the input from the user by the "," and stores it in a list
# there is also an exception for when the incorrect input is not right.
for operations in test_cases:
    print(f"\nPerforming {operations} operations:")
# this loop iterates through every input in the test case list. and performs the actions below
    # Measure time for floating-point multiplication
    start_time = time.time()
    float_multi(operations)
    float_time = time.time() - start_time
    print(f"Floating-point multiplication time: {float_time: .4f} seconds")

    # Measure time for integer multiplication
    start_time = time.time()
    int_multi(operations)
    int_time = time.time() - start_time
    print(f"Integer multiplication time: {int_time: .4f} seconds")

    # Compare times
    print(f"Difference: {abs(float_time - int_time): .4f} seconds")
# I called the functions for each one of the inputs in the test_cases and then prints out the result and differences.