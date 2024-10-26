def generate_fibonacci(n):
    fibonacci_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b  # Update to the next Fibonacci numbers
    
    return fibonacci_sequence

# Get the number of terms from the user
num_terms = int(input("Enter the number of Fibonacci terms to generate: "))
fibonacci_numbers = generate_fibonacci(num_terms)

print(f"The first {num_terms} terms of the Fibonacci sequence are: {fibonacci_numbers}")
