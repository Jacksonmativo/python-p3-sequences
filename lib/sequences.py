#!/usr/bin/env python3

def print_fibonacci(length):
    # Generate the Fibonacci sequence up to the given length
    if length <= 0:
        fibonacci = []
    elif length == 1:
        fibonacci = [0]
    else:
        fibonacci = [0, 1]
        while len(fibonacci) < length:
            fibonacci.append(fibonacci[-1] + fibonacci[-2])
    # Print the sequence
    print(fibonacci)
    # Return the sequence for testing
    return fibonacci
