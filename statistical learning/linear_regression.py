def fibonacci(n):
    fib_seq = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])  # Add the sum of the previous two numbers to the sequence
    return fib_seq

n = 10  # Number of Fibonacci numbers to generate
fib_numbers = fibonacci(n)
print(fib_numbers)
