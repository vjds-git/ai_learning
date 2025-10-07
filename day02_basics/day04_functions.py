# Function definition
def greet(name):
    return f"Hello, {name}!"

# Function with default argument
def add(a, b=0):
    return a + b

# Function with multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

# Call functions
print(greet("Sam"))
print(add(10, 5))
print(add(7))  # uses default b=0
low, high = min_max([3, 8, 2, 10])
print("Lowest:", low, "Highest:", high)
