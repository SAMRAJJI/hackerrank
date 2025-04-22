cube = lambda x: x**3  # Lambda function to cube a number

def fibonacci(n):
    # Generate the first n Fibonacci numbers
    fib_list = [0, 1]  # Start with 0 and 1
    for _ in range(2, n):  # Generate until we have n numbers
        fib_list.append(fib_list[-1] + fib_list[-2])  # Add last two numbers
    return fib_list[:n]  # Ensure only n numbers are returned

if __name__ == '__main__':
    n = int(input())  # Input the number of Fibonacci numbers
    print(list(map(cube, fibonacci(n))))  # Cube each Fibonacci number and print
