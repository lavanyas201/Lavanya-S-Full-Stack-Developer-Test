# Problem-2: Generate a series of odd numbers until a = x

def generate_series(n):
    result = []
    for i in range(n):
        result.append(2 * i + 1)
    return result

# Example usage
a = int(input("Enter a number: "))
print("Output:", generate_series(a))
