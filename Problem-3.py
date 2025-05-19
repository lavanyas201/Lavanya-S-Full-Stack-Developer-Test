# Problem-3: Generate a series of odd numbers up to a maximum of the largest odd number ≤ input

def generate_series(n):
    result = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            result.append(i)
    return result

# Example usage
a = int(input("Enter a number: "))
print("Output:", generate_series(a))
